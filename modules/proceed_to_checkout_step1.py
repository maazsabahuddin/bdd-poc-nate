import time
from selenium.common import exceptions
# Local imports
from utility.constants import Pattern, Tags, Timer
from utility.utilities import Utils


class ProceedToCheckoutStep1():

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web

    def find_cart(self):
        view_cart_dict = self.extract_required_elements(Pattern.VIEW_CART)
        required_tag = Utils.get_required_tag(view_cart_dict.keys(), Tags.POSSIBLE_VIEW_CART)
        self.required_element = Utils.get_required_element(required_tag, view_cart_dict)
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, Tags.POSSIBLE_VIEW_CART)
    
    def hit_button_to_proceed(self):
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            print("In exception")
            parent_element = self.web.find_parent_element_from_child(self.required_element)
            parent_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
