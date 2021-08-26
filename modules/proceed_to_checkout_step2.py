from modules.constants import Pattern
from modules.constants import Tags
from modules.utilities import Utils
from selenium.common import exceptions

import time

class ProceedToCheckoutStep2():
    
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web

    def find_cart_checkout(self):
        view_cart_dict = self.extract_required_elements(Pattern.VIEW_CART_CHECKOUT)
        required_tag = Utils.get_required_tag(view_cart_dict.keys(), Tags.POSSIBLE_VIEW_CART)
        self.required_element = Utils.get_required_element_by_key(required_tag, view_cart_dict, "ProceedToCheckoutStep2")
        print("-------> checking element is enabled ", self.required_element.is_enabled())
        print("-------> checking element is displayed ", self.required_element.is_displayed())
        time.sleep(self.web.process_pause_time)

    def extract_required_elements(self, pattern):
        try:
            add_to_elements = self.web.finds_by_xpath_wait(pattern)
            return Utils.create_dict(add_to_elements)
        except:
            return {}

    def hit_button_to_proceed(self):
        try:
            # print(self.required_element.get_attribute("outerHTML"))
            self.required_element.click()
            time.sleep(self.web.process_pause_time)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            parent_element = self.web.find_parent_element_from_child(self.required_element)
            # print(parent_element.get_attribute("outerHTML"))
            parent_element.click()
            time.sleep(self.web.process_pause_time)