# Python imports
import time

# Local imports
from utility.constants import Pattern, TagsList, Timer
from utility.utilities import Utils


class CardDetails:

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.is_card_details_found = False
        self.card_holder_name_element = None
        self.card_number = None
        self.card_month_expiry_element = None
        self.card_year_expiry_element = None
        self.card_cvv_element = None
        
    def find_card_details_elements(self):
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        element_count = 0
        
        card_holder_name_dict = self.__extract_required_elements(Pattern.CARD_HOLDER_NAME)
        card_number_dict = self.__extract_required_elements(Pattern.CARD_NUMBER)
        card_month_expiry_dict = self.__extract_required_elements(Pattern.EXPIRATION_MONTH)
        card_year_expiry_dict = self.__extract_required_elements(Pattern.EXPIRATION_YEAR)
        card_cvv_dict = self.__extract_required_elements(Pattern.CVV)

        if card_holder_name_dict:
            card_holder_name_tag = \
                Utils.get_required_tag(card_holder_name_dict.keys(), TagsList.POSSIBLE_CARD_ELEMENTS)
            self.card_holder_name_element = Utils.get_required_element(card_holder_name_tag, card_holder_name_dict)
            if self.card_holder_name_element:
                element_count = element_count + 1

        card_number_tag = \
            Utils.get_required_tag(card_number_dict.keys(), TagsList.POSSIBLE_CARD_ELEMENTS)
        self.card_number_element = Utils.get_required_element(card_number_tag, card_number_dict)
        if self.card_number_element:
            element_count = element_count + 1
        
        card_month_expiry_tag = \
            Utils.get_required_tag(card_month_expiry_dict.keys(), TagsList.POSSIBLE_CARD_ELEMENTS)
        self.card_month_expiry_element = Utils.get_required_element(card_month_expiry_tag, card_month_expiry_dict)
        if self.card_month_expiry_element:
            element_count = element_count + 1

        if card_year_expiry_dict:
            card_year_expiry_tag = \
                Utils.get_required_tag(card_year_expiry_dict.keys, TagsList.POSSIBLE_CARD_ELEMENTS)
            self.card_year_expiry_element = Utils.get_required_element(card_year_expiry_tag, card_year_expiry_dict)
            if self.card_year_expiry_element:
                element_count = element_count + 1

        card_cvv_tag = \
            Utils.get_required_tag(card_cvv_dict.keys, TagsList.POSSIBLE_CARD_ELEMENTS)
        self.card_cvv_element = Utils.get_required_element(card_cvv_tag, card_cvv_dict)
        if self.card_cvv_element:
            element_count = element_count + 1

        if element_count >= 3:
            self.is_card_details_found = True


    def __extract_required_elements(self, pattern):
        add_to_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(add_to_elements, TagsList.POSSIBLE_CARD_ELEMENTS)

    
    def select_and_populate_card_details(self, card_number, card_holder_name, card_month_expiry, card_year_expiry, card_cvv, card_expiry):
        self.card_number_element.send_keys(card_number)
        time.sleep(Timer.ONE_SECOND_TIMEOUT)
        if not self.card_year_expiry_element is None:
            self.card_month_expiry_element.send_keys(card_month_expiry)
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            self.card_year_expiry_element.send_keys(card_year_expiry)
        else:
            self.card_month_expiry_element.send_keys(card_expiry)
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
        self.card_cvv_element.send_keys(card_cvv)
        time.sleep(Timer.ONE_SECOND_TIMEOUT)
        if self.card_holder_name_element != None:
            self.card_holder_name_element.send_keys(card_holder_name)
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        
