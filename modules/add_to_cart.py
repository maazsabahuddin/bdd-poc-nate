from logging import exception
import time

from selenium.common import exceptions
from modules.utilities import Utils
from modules.constants import Pattern, Tags

class AddToCart():
    def __init__(self, context):
        self.context = context
        self.web = context.web
    
    def find_add_to_(self):
        add_to_dict = self.extract_required_elements(Pattern.ADD_TO_NEW_PAT)
        if (add_to_dict == {}):
            add_to_dict = self.extract_required_elements(Pattern.ADD_TO_PATTERN)
        required_tag = Utils.get_required_tag(add_to_dict.keys(), Tags.POSSIBLE_ADD_TO_TAGS_LIST)
        print(required_tag)
        self.required_element = Utils.get_required_element_by_key(required_tag, add_to_dict, "AddToCart")
        time.sleep(self.web.process_pause_time)

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, Tags.POSSIBLE_ADD_TO_TAGS_LIST)

    
    def hit_add_to_cart_element(self):
        try:
            self.required_element.click()
            time.sleep(self.web.process_pause_time)
        except exceptions.ElementClickInterceptedException as e:
            print("exception found ", e)
        except exceptions.ElementClickInterceptedException:
            print(self.required_element)

    def check_cookies_overlay(self):
        is_cookies_overlay = Utils.accept_cookies(self.web.find_by_xpath_wait)
        if (is_cookies_overlay):
            time.sleep(self.web.process_pause_time)
            self.find_add_to_()
        return is_cookies_overlay
    
    def is_closeable_overlay(self):
        try:
            cross_element = self.web.find_by_xpath_wait("//*[contains(@aria-label,'Close Menu') or contains(@aria-label,'Close')]")
            if (cross_element is not None):
                cross_element.click()
                time.sleep(self.web.process_pause_time)
                self.find_add_to_()
                return True
            else:
                return False
        except (exceptions.TimeoutException, exceptions.ElementClickInterceptedException) as e:
            return False
