# Python Imports
import time

# Local Imports
from features.environment import failed_case
from modules.logger import logger
from utility.constants import Timer, TagsList, Pattern
from utility.utilities import Utils


class ContinueToPayment:
    """
    This class is responsible to fill out shipping address details by identify
    shipping page type and other flows.
    """
    def __init__(self, context):
        self.context = context
        self.web = context.web
        logger.info("Initializing payment variable.")
        self.payment_element = None

    def click_payment_button(self):
        logger.info("clicking on payment button")
        try:
            self.payment_element.click()
        except Exception as e:
            logger.info("Element is not clickable")
            failed_case(scenario="ContinueToPayment Button Flow", exception_message=str(e))

        logger.info(f"{Timer.PROCESS_PAUSE_TIMEOUT} seconds pause timeout")
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        logger.info("TIMEOUT OVER")

    def find_required_element(self):
        self.web.open(self.context.url)
        time.sleep(60)
        logger.info("finding payment element")
        continue_to_pay_element = self.web.finds_by_xpath_wait(Pattern.PAYMENT)
        element_dict = Utils.fetch_required_elements(continue_to_pay_element, TagsList.POSSIBLE_CONTINUE_BUTTON)
        if not element_dict:
            return
        logger.info("found")
        self.payment_element = Utils.get_required_element_2(element_dict, TagsList.POSSIBLE_CONTINUE_TO_PAYMENT_BUTTON)        

    def validate_payment_fields(self):
        """
        Validate if payment field found or not..
        """
        return True if self.payment_element else False
