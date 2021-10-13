# Python imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from file import close_file
from modules.logger import logger
from utility.utilities import Utils
from utility.constants import Pattern, TagsList, Timer, ETC
from app import _result_file


class AddToCart:

    def __init__(self, context):
        self.context = context
        self.web = context.web
        self.required_element = None
        self.is_add_to_cart_found = False
        self.color_element = None
        self.size_element = None
        self.required_element = None
        self.is_cart_flow = False

    def find_add_to_(self):

        self.web.open(self.context.url[0])
        self.web.scroll_page(0, 30)

        if len(self.context.url) > 1:
            logger.info("Cart flow execution..")
            self.is_cart_flow = True
            for idx, site in enumerate(self.context.url[1:]):
                self.context.web.open_another_tab(url=site, tab_name=ETC.NUMBER_CONFIG.get(idx+2)+"tab")
            return

        time.sleep(Timer.FIVE_SECOND_TIMEOUT)
        add_to_dict = self.extract_required_elements(Pattern.ADD_TO_PATTERN)
        if not add_to_dict:
            logger.info("Add to cart element not found..")
            return

        self.required_element = Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
        if self.required_element:
            self.is_add_to_cart_found = True
        else:
            logger.info("finding for overlays")
            is_overlays_found_and_close = Utils.check_overlays(self.context)
            logger.info(f"is overlay handled: {is_overlays_found_and_close}")
            time.sleep(Timer.FIVE_SECOND_TIMEOUT)
            if is_overlays_found_and_close:
                self.required_element = Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
                self.is_add_to_cart_found = True if self.required_element else False

    @staticmethod
    def get_size_or_color_xpath(element):
        """
        :param element: This element is dictionary either color or size
        :return:
        """
        size_xpath = ""
        for key, value in element.items():
            if key == list(element.keys())[-1]:
                size_xpath += f"contains(@{key}, '{value}')"
                break
            size_xpath += f"contains(@{key}, '{value}') and "

        return size_xpath

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        self.color_element = \
            self.web.finds_by_xpath_wait(f"//*[{AddToCart.get_size_or_color_xpath(self.context.color)}]")
        self.size_element = \
            self.web.finds_by_xpath_wait(f"//*[{AddToCart.get_size_or_color_xpath(self.context.size)}]")

        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)

    def select_color_size(self):
        if self.color_element:
            logger.info("Selecting color")
            self.color_element[0].click()
        if self.size_element:
            logger.info("Selecting size")
            try:
                self.size_element[0].click()
            except exceptions.StaleElementReferenceException:
                size_element = \
                    self.web.finds_by_xpath_wait(f"//*[{AddToCart.get_size_or_color_xpath(self.context.size)}]")
                size_element[0].click()

    def hit_add_to_cart_element(self):
        try:
            self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException,
                AttributeError) as e:
            logger.info(f"\nIn exception of add to cart button.. {str(e)}\n")
            logger.info("finding for overlays")
            is_overlays_found_and_close = Utils.check_overlays(self.context)
            logger.info(f"is overlay handled: {is_overlays_found_and_close}")
            time.sleep(Timer.FIVE_SECOND_TIMEOUT)
            if is_overlays_found_and_close:
                self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
            else:
                logger.info("Exception caught at Add to Cart Flow")
                logger.info("Skipping all other scenarios.")
                _result_file.write(f"{self.context.name} - FAILED - Step Add to Cart - {str(e)}\n") \
                    if self.context.log == "True" else None
                close_file(_result_file)
                self.context._root[ETC.IS_CASE_FAILED] = True
                self.context.web.skip_all_remaining_scenarios()
    
    def __click_and_wait_for(self, timer):
        self.required_element.click()
        time.sleep(timer)

    def cart_flow_(self, counter):
        """
        This function is responsible to fetch add to cart element, click on it and perform this recursively
        until base condition met....
        """

        logger.info("Switching tab ") if counter != len(self.context.web.web_driver.window_handles) \
            else logger.info("last tab")

        if counter == len(self.context.web.web_driver.window_handles):
            return

        # for tab in self.context.web.web_driver.window_handles[:len(self.context.web.web_driver.window_handles)]:

        self.web.scroll_page(0, 30)
        time.sleep(Timer.FIVE_SECOND_TIMEOUT)
        add_to_dict = self.extract_required_elements(Pattern.ADD_TO_PATTERN)
        if not add_to_dict:
            logger.info("Add to cart element not found..")
            return

        self.required_element = Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
        if self.required_element:
            self.is_add_to_cart_found = True
            self.hit_add_to_cart_element()
        else:
            logger.info("finding for overlays")
            is_overlays_found_and_close = Utils.check_overlays(self.context)
            logger.info(f"is overlay handled: {is_overlays_found_and_close}")
            time.sleep(Timer.FIVE_SECOND_TIMEOUT)
            if is_overlays_found_and_close:
                self.required_element = \
                    Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
                self.is_add_to_cart_found = True if self.required_element else False
                self.hit_add_to_cart_element() if self.is_add_to_cart_found else None

            # if tab == self.context.web.web_driver.window_handles[-1]:
            #     return

        self.context.web.web_driver.switch_to.window(self.context.web.web_driver.window_handles[counter])
        self.context.web.web_driver.refresh()

        return self.cart_flow_(counter+1)
