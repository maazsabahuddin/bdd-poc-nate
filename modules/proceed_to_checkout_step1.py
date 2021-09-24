# Local imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from modules.logger import logger
from utility.constants import Pattern, TagsList, Timer, ETC
from utility.utilities import Utils


class ProceedToCheckoutStep1:

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.required_element = None
        self.is_checkout_found = False

    def find_cart(self):
        view_cart_dict = self.extract_required_elements(Pattern.VIEW_CART)
        if not view_cart_dict:
            return
        required_tag = Utils.get_required_tag(view_cart_dict.keys(), TagsList.POSSIBLE_VIEW_CART)
        self.required_element = Utils.get_required_element(required_tag, view_cart_dict)
        self.is_checkout_found = True
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_VIEW_CART)
    
    def hit_button_to_proceed(self):
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            logger.info("Exception caught at Proceed to Checkout Step 1")
            logger.info("Skipping all other scenarios.")
            self.context._root[ETC.IS_CASE_FAILED] = True
            self.context.web.skip_all_remaining_scenarios()
