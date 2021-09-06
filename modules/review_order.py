# Python imports
import time

# Local imports
from utility.constants import Pattern, TagsList, Timer
from utility.utilities import Utils

class ReviewOrder:
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.is_review_order_found = False
        self.required_element = None

    def find_review_order(self):
        self.web.open(self.context.url)
        time.sleep(150)
        reivew_order_elements_dict = self.__extract_required_elements(Pattern.REVIEW_ORDER)
        if not reivew_order_elements_dict:
            return
        required_tag = Utils.get_required_tag(reivew_order_elements_dict.keys(), TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)
        required_element = Utils.get_required_element(required_tag, reivew_order_elements_dict)
        if required_element is not None:
            self.is_review_order_found = True
        self.required_element = required_element

    def __extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)

    def hit_review_order(self):
        self.required_element.click()
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)