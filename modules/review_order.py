# Python imports
import time

# Local imports
from features.environment import failed_case
from utility.constants import Pattern, TagsList, Timer
from utility.utilities import Utils
from modules.logger import logger


class ReviewOrder:

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.is_review_order_found = False
        self.review_order_element = None
        self.shipping_address_elements = None

    def find_review_order(self):
        review_order_elements_dict = self.__extract_required_elements(Pattern.REVIEW_ORDER, Pattern.SHIPPING_ADDRESS)
        if not review_order_elements_dict:
            logger.info("review order element not found.")
            return
        required_tag = \
            Utils.get_required_tag(review_order_elements_dict.keys(), TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)
        required_element = Utils.get_required_element(required_tag, review_order_elements_dict)
        if required_element is not None:
            logger.info("Review order required element found.")
            self.is_review_order_found = True
        self.review_order_element = required_element

    def __extract_required_elements(self, pattern, shipping_pattern):
        """
        This shipping address element will click the input tag 'same as shipping address'.
        :param pattern:
        :param shipping_pattern:
        :return:
        """
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        self.shipping_address_elements = self.web.finds_by_xpath_wait(shipping_pattern)
        if self.shipping_address_elements:
            logger.info("Found same as shipping address input tag..")
            logger.info("Clicking now..")
            self.shipping_address_elements[0].click()
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_CONFIRM_AND_PAY_ELEMENTS)

    def hit_review_order(self):
        try:
            self.review_order_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except Exception as e:
            failed_case(context=self.context, scenario="Review Order", exception_message=str(e))
