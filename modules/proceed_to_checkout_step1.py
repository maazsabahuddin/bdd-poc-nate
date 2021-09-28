# Local imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from file import close_file
from modules.logger import logger
from utility.constants import Pattern, TagsList, Timer, ETC
from utility.utilities import Utils
from app import _result_file


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
        self.required_element = Utils.get_required_element_2(view_cart_dict, TagsList.POSSIBLE_VIEW_CART)
        if self.required_element:
            self.is_checkout_found = True
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_VIEW_CART)
    
    def hit_button_to_proceed(self):
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException,
                AttributeError) as e:
            logger.info(f"Exception caught at Proceed to Checkout Step 1 due to {str(e)}")
            logger.info("Skipping all other scenarios.")
            _result_file.write(f"\n{self.context.name} - FAILED - Step Checkout Step1 - {str(e)}\n") \
                if self.context.log == "True" else None
            close_file(_result_file)
            self.context._root[ETC.IS_CASE_FAILED] = True
            self.context.web.skip_all_remaining_scenarios()
