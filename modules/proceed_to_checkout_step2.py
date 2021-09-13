# Python imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from utility.constants import Pattern, TagsList, Timer
from utility.utilities import Utils


class ProceedToCheckoutStep2:
    
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.required_element = None

    def find_cart_checkout(self):
        view_cart_dict = self.extract_required_elements(Pattern.VIEW_CART_CHECKOUT)
        self.required_element = Utils.get_required_element_2(view_cart_dict, TagsList.POSSIBLE_VIEW_CART)
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_VIEW_CART)

    def hit_button_to_proceed(self):
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            parent_element = self.web.find_parent_element_from_child(self.required_element)
            parent_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
