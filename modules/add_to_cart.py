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
        self.web.open(self.context.url)
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

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)

    def hit_add_to_cart_element(self):
        try:
            self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            logger.info(f"\nIn exception of add to cart button.. {str(e)}\n")
            logger.info("finding for overlays")
            is_overlays_found_and_close = Utils.check_overlays(self.context)
            logger.info(f"is overlay handled: {is_overlays_found_and_close}")
            if is_overlays_found_and_close:
                self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
    
    def __click_and_wait_for(self, timer):
        self.required_element.click()
        time.sleep(timer)
