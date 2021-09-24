# Python imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from modules.logger import logger
from utility.constants import Pattern, TagsList, Timer, ETC
from utility.utilities import Utils


class ProceedToCheckoutStep2:
    
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.required_element = None

    def find_cart_checkout(self):
        view_cart_dict = self.extract_required_elements(Pattern.VIEW_CART_CHECKOUT)
        if not view_cart_dict:
            is_overlays_found_and_close = Utils.check_overlays(context=self.context)
            if is_overlays_found_and_close:
                view_cart_dict = self.extract_required_elements(Pattern.VIEW_CART_CHECKOUT)
            else:
                return
        self.required_element = Utils.get_required_element_2(view_cart_dict, TagsList.POSSIBLE_VIEW_CART)

    def extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_VIEW_CART)

    def hit_button_to_proceed(self):
        try:
            self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.ElementNotInteractableException, exceptions.ElementClickInterceptedException) as e:
            is_overlays_found_and_close = Utils.check_overlays(context=self.context)
            if is_overlays_found_and_close:
                self.__click_and_wait_for(Timer.PROCESS_PAUSE_TIMEOUT)
            else:
                logger.info("Exception caught at Checkout Step 2")
                logger.info("Skipping all other scenarios.")
                self.context._root[ETC.IS_CASE_FAILED] = True
                self.context.web.skip_all_remaining_scenarios()

    def __click_and_wait_for(self, timer):
        self.required_element.click()
        time.sleep(timer)
