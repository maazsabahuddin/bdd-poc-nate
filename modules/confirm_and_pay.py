# Python imports
import time

# Local imports
from features.environment import failed_case
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
            confirm_pay_elements_dict = self.__extract_required_elements(Pattern.PLACE_ORDER)
        if not confirm_pay_elements_dict:
            return
        required_tag = \
            Utils.get_required_tag(confirm_pay_elements_dict.keys(), TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)
        required_element = Utils.get_required_element(required_tag, confirm_pay_elements_dict)
        if required_element is not None:
            self.is_confirm_and_pay_found = True
        self.required_element = required_element

    def __extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)

    def hit_confirm_and_pay(self):
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except Exception as e:
            failed_case(scenario="Confirm And Pay", exception_message=str(e))
