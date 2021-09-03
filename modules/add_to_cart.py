import time
from selenium.common import exceptions
# Local imports
from utility.utilities import Utils
from utility.constants import Pattern, Tags, Timer

class AddToCart():
    def __init__(self, context):
        self.context = context
        self.web = context.web
        self.is_add_to_cart_found = False
    
    def find_add_to_(self):
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        add_to_dict = self.extract_required_elements(Pattern.ADD_TO_PATTERN)
        if not add_to_dict:
            return
        required_tag = Utils.get_required_tag(add_to_dict.keys(), Tags.POSSIBLE_ADD_TO_TAGS_LIST)
        required_element = Utils.get_required_element(required_tag, add_to_dict)
        if required_element is not None:
            self.is_add_to_cart_found = True
        self.required_element = required_element

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, Tags.POSSIBLE_ADD_TO_TAGS_LIST)

    def hit_add_to_cart_element(self):
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            print('hit_add_to_cart_element: ', e)
            # handling of overlays and pop-ups
            return

    def check_cookies_overlay(self):
        is_cookies_overlay = Utils.accept_cookies(self.web.find_by_xpath_wait)
        if (is_cookies_overlay):
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
            self.find_add_to_()
        return is_cookies_overlay
    
    def is_closeable_overlay(self):
        try:
            cross_element = self.web.find_by_xpath_wait("//*[contains(@aria-label,'Close Menu') or contains(@aria-label,'Close')]")
            if (cross_element is not None):
                cross_element.click()
                time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
                self.find_add_to_()
                return True
            else:
                return False
        except (exceptions.TimeoutException, exceptions.ElementClickInterceptedException) as e:
            print("is_closeable_overlay: ", e)
            return False
