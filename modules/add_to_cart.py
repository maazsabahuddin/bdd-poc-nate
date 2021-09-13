# Python imports
from modules.cookies_pop_up import CookiesPopUp
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from utility.utilities import Utils
from utility.constants import Pattern, TagsList, Timer
from modules.logger import logger


class AddToCart:

    def __init__(self, context):
        self.context = context
        self.web = context.web
        self.required_element = None
        self.is_add_to_cart_found = False
        self.required_element = None
    
    def find_add_to_(self):
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        add_to_dict = self.extract_required_elements(Pattern.ADD_TO_PATTERN)
        if not add_to_dict:
            return

        # required_tag = Utils.get_required_tag(add_to_dict.keys(), TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
        self.required_element = Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
        if self.required_element is not None:
            self.is_add_to_cart_found = True
        else:
            is_overlay_found_and_close = self.__check_for_overlay(self.context)
            if is_overlay_found_and_close:
                self.required_element = Utils.get_required_element_2(add_to_dict, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)
                if self.required_element is not None:
                    self.is_add_to_cart_found = True

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)

    def hit_add_to_cart_element(self):
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            # handling of overlays and pop-ups
            self.__check_for_overlay(self.context)
            return

    def __check_for_overlay(self, context):
        logger.info("In cookies overlay function")
        cookies_pop_up = CookiesPopUp(context)
        logger.info("finding for cookies element")
        cookies_pop_up.find_accept_cookies()
        logger.info("trying to click on cookies element")
        cookies_pop_up.accept_cookies()

    def check_cookies_overlay(self):
        is_cookies_overlay = Utils.accept_cookies(self.web.find_by_xpath_wait)
        if is_cookies_overlay:
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
            self.find_add_to_()

        return is_cookies_overlay
    
    def is_closeable_overlay(self):
        try:
            cross_element = \
                self.web.find_by_xpath_wait("//*[contains(@aria-label,'Close Menu') or contains(@aria-label,'Close')]")
            if cross_element is not None:
                cross_element.click()
                time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
                self.find_add_to_()
                return True
            else:
                return False
        except (exceptions.TimeoutException, exceptions.ElementClickInterceptedException) as e:
            logger.info(str(e))
            logger.info("is_closeable_overlay: ", e)
            return False
