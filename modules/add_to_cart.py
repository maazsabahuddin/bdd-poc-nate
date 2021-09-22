# Python imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from modules.logger import logger
from utility.utilities import Utils
from utility.constants import Pattern, TagsList, Timer


class AddToCart:

    def __init__(self, context):
        self.context = context
        self.web = context.web
        self.required_element = None
        self.is_add_to_cart_found = False
        self.required_element = None
    
    def find_add_to_(self):
        self.web.scroll_page(0, 30)
        time.sleep(Timer.FIVE_SECOND_TIMEOUT)
        add_to_dict = self.extract_required_elements(Pattern.ADD_TO_PATTERN)
        if not add_to_dict:
            return

        self.required_element = Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
        if self.required_element:
            self.is_add_to_cart_found = True
        else:
            logger.info("finding for overlays")
            is_overlays_found_and_close = Utils.check_overlays(self.context)
            logger.info(f"is overlay handled: {is_overlays_found_and_close}")
            if is_overlays_found_and_close:
                self.required_element = Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
                if self.required_element:
                    self.is_add_to_cart_found = True

    def get_color_xpath(self):
        # color_xpath = ""
        for key, value in self.context.color.items():
            print(key, value)
        # color_class = self.context.color['class'] if self.context.color else ""
        # color_data_index = self.context.color['data-index'] if self.context.color else ""

    def get_size_xpath(self):
        # size_xpath = "
        for key, value in self.context.size.items():
            print(key, value)
        # size_class = self.context.size['class'] if self.context.size else ""
        # size_data_index = self.context.size['data-index'] if self.context.size else ""

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        self.get_color_xpath()
        self.get_size_xpath()
        # color_element = self.web.finds_by_xpath_wait(f"//*[contains(@class, {color_class}) "
        #                                              f"and contains(@data-index, {color_data_index})]")
        # size_element = self.web.finds_by_xpath_wait(f"//*[contains(@class, {size_class}) "
        #                                             f"and contains(@data-index, {size_data_index})]")
        # print(color_element)
        # print(size_element)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)

    def hit_add_to_cart_element(self):
        try:
            self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            logger.info(f"In exception of add to cart button.. {str(e)}")
            is_overlays_found_and_close = Utils.check_overlays(self.context)
            logger.info(is_overlays_found_and_close)
            if is_overlays_found_and_close:
                self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
    
    def __click_and_wait_for(self, timer):
        self.required_element.click()
        time.sleep(timer)
