# Python Imports
import time

# Local Imports
from features.environment import failed_case
from utility import constants
from modules.logger import logger
from utility.constants import Timer
from utility.utilities import Utils


class Payment:
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
        continue_elements_dict = \
            Utils.fetch_required_elements(self.payment_element,
                                          constants.TagsList.POSSIBLE_PAYMENT_BUTTON)
        if not continue_elements_dict:
            logger.info("Button element not found.")
            self.context.scenario.skip(reason='cannot find payment field')

        extracted_element_tag = Utils.get_required_tag(continue_elements_dict.keys(),
                                                       constants.TagsList.POSSIBLE_CONTINUE_BUTTON)
        required_element = Utils.get_required_element(extracted_element_tag, continue_elements_dict)
        if not required_element:
            logger.info(f"{extracted_element_tag} element is not clickable")

        try:
            required_element.click()
        except Exception as e:
            logger.info("Element is not clickable")
            failed_case(scenario="Payment Button Flow", exception_message=str(e))
            # self.context.scenario.skip(reason='cannot find payment field')

        logger.info(f"{Timer.PROCESS_PAUSE_TIMEOUT} seconds pause timeout")
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        logger.info("TIMEOUT OVER")

    def fetching_required_elements(self):
        logger.info("fetching payment element")
        self.payment_element = self.web.finds_by_xpath_wait(constants.Pattern.PAYMENT)
        logger.info("Fetched")

    def validate_payment_fields(self):
        """
        Validate if payment field found or not..
        """
        return True if self.payment_element else False
