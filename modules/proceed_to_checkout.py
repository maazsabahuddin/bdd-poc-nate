import time

from modules.constants import Pattern, Tags
from modules.utilities import Utils
from selenium.common import exceptions

class ProceedToCheckout():

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web

    def find_cart(self):
        view_cart_dict = self.extract_required_elements(Pattern.VIEW_CART)
        required_tag = Utils.get_required_tag(view_cart_dict.keys(), Tags.POSSIBLE_VIEW_CART)
        self.required_element = Utils.get_required_element_by_key(required_tag, view_cart_dict, "ProceedToCheckout")
        print("------> required tag: ", self.required_element)
        print("------> tag: ", self.required_element.get_attribute("outerHTML"))
        time.sleep(self.web.process_pause_time)

    def extract_required_elements(self, pattern):
        try:
            add_to_elements = self.web.finds_by_xpath_wait(pattern)
            print("------> add to element: ", add_to_elements)
            return Utils.create_dict(add_to_elements)
        except:
            return {}
    
    def hit_button_to_proceed(self):
        try:
            self.required_element.click()
            time.sleep(self.web.process_pause_time)
        except exceptions.ElementClickInterceptedException as e:
            print("exception found ", e)
        except exceptions.ElementClickInterceptedException:
            print(self.required_element)