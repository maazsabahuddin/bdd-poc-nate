# Python imports
import time

# Local imports
from features.environment import failed_case
from modules.logger import logger
from utility.constants import Pattern, TagsList, Timer
from utility.utilities import Utils


class ConfirmAndPay:

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.is_confirm_and_pay_found = False
        self.required_element = None
    
    def find_confirm_and_pay(self):
        confirm_pay_elements_dict = self.__extract_required_elements(Pattern.CONFIRM_AND_PAY)
        if not confirm_pay_elements_dict:
            logger.info("Confirm and pay element not found..")
            return
        required_element = Utils.get_required_element_2(confirm_pay_elements_dict, TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)
        if required_element:
            self.is_confirm_and_pay_found = True
        self.required_element = required_element

    def __extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)

    def hit_confirm_and_pay(self):
        try:
            logger.info("Clicking on confirm and pay element")
            self.required_element.click()
            logger.info("------------> Waiting for 60secs to view response.")
            time.sleep(60)
        except Exception as e:
            failed_case(context=self.context, scenario="Confirm And Pay", exception_message=str(e))
