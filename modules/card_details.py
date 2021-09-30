# Python imports
import logging
import time

# Local imports
from utility.constants import Pattern, Tags, TagsList, Timer, ETC, UserInfo
from utility.utilities import Utils

# Framework imports
from selenium.common import exceptions


class CardDetails:

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.is_card_details_found = False
        self.card_holder_name_element = None
        self.card_number_element = None
        self.card_month_expiry_element = None
        self.card_year_expiry_element = None
        self.card_cvv_element = None
        self.card_elements_iframes = None
        self.email_element = None
        self.continue_button = None
        
    def find_card_details_elements(self):
        self.web.open(self.context.url)
        time.sleep(40)
        self.__update_card_type_details_if_any(Pattern.CARD_TYPE)
        self.__scrap_required_elements()
        self.is_card_details_found = self.__is_required_fields_found()
        self.email_element = self.__extract_email_element()
        self.continue_button = self.__extract_continue_button()
        if not self.is_card_details_found:
            self.find_required_iframe()

    def __get_required_element(self, pattern):
        extracted_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.extract_required_element_2(list_of_elements=extracted_elements)

    def __extract_required_elements(self, pattern, posible_elements_list):
        required_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(required_elements, posible_elements_list)
    
    def select_and_populate_card_details(self, card_number, card_holder_name, card_month_expiry, card_year_expiry, card_cvv, card_expiry, email):
        if self.card_number_element:
            self.__populate_card_number(number=card_number)
        if self.card_month_expiry_element:
            self.__populate_card_expiration_details(month=card_month_expiry, year=card_year_expiry, m_y=card_expiry)
        if self.card_holder_name_element:
            self.__populate_card_holder_name(name=card_holder_name)
        if self.card_cvv_element:
            self.__populate_card_security_code(cvv=card_cvv)
        if self.email_element:
            self.__populate_email(email=email)
        if self.continue_button:
            self.__continue()
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def __populate_month(self, month):
        if self.card_month_expiry_element.tag_name == Tags.SELECT:
            all_options = self.card_month_expiry_element.find_elements_by_tag_name(ETC.OPTION)
            for option in all_options:
                if option.get_attribute(ETC.VALUE) == UserInfo.CARD_EXPIRATION_MONTH:
                    option.click()
                    break
        else:
            expiry_details = month.split("/")
            self.card_month_expiry_element.send_keys(expiry_details[0])
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            self.card_month_expiry_element.send_keys(expiry_details[1])
        time.sleep(Timer.THREE_SECOND_TIMEOUT)

    def __populate_year(self, year):
        if self.card_year_expiry_element.tag_name == Tags.SELECT:
            all_options = self.card_year_expiry_element.find_elements_by_tag_name(ETC.OPTION)
            for option in all_options:
                if option.get_attribute(ETC.VALUE) == UserInfo.CARD_EXPIRATION_YEAR:
                    option.click()
                    break
        else:
            self.card_year_expiry_element.send_keys(year)
        time.sleep(Timer.THREE_SECOND_TIMEOUT)

    def __populate_card_holder_name(self, name):
        try:
            self.card_holder_name_element.send_keys(name)
            time.sleep(Timer.THREE_SECOND_TIMEOUT)
        except Exception as e:
            print(f"Exception while populating holder name of {e}")

    def __populate_card_number(self, number):
        try:
            card_number = number.split(" ")
            self.card_number_element.send_keys(card_number[0])
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            self.card_number_element.send_keys(card_number[1])
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            self.card_number_element.send_keys(card_number[2])
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            self.card_number_element.send_keys(card_number[3])
            time.sleep(Timer.THREE_SECOND_TIMEOUT)
        except Exception as e:
            print(f"Exception while populating number of {e}")

    def __populate_card_security_code(self, cvv):
        try:
            self.card_cvv_element.send_keys(cvv)
            time.sleep(Timer.THREE_SECOND_TIMEOUT)
        except Exception as e:
            print(f"Exception while populating cvv of {e}")

    def __populate_card_expiration_details(self, month, year, m_y):
        try:
            if self.card_year_expiry_element:
                self.__populate_month(month=month)
                self.__populate_year(year=year)
            else:
                self.__populate_month(month=m_y)
        except Exception as e:
            print(f"Exception while populating expiry of {e}")

    def __update_card_type_details_if_any(self, pattern):
        extracted_elements = self.web.finds_by_xpath_wait(pattern)
        card_type_dict = Utils.fetch_required_elements3(extracted_elements, TagsList.POSSIBLE_CARD_TYPE_ELEMENTS)
        card_type_element = Utils.get_required_element_2(card_type_dict, TagsList.POSSIBLE_CARD_TYPE_ELEMENTS)
        self.__select_card_type(element=card_type_element)

    def __select_card_type(self, element):
        if not element:
            return
        if element.tag_name == Tags.SELECT:
            all_options = element.find_elements_by_tag_name(ETC.OPTION)
            for option in all_options:
                if option.get_attribute(ETC.TEXT) in UserInfo.CARD_TYPE:
                    option.click()
                    break
        else:
            try:
                element.click()
            except exceptions.ElementNotInteractableException:
                parent_element = Utils.find_parent_element_from_child(child_element=element, filter_list=["label"])
                if parent_element:
                    parent_element.click()
                else:
                    element_id = element.get_attribute("id")
                    sibling_elements = self.web.find_by_xpath(f"//label[@for={element_id}]")
                    if not sibling_elements:
                        return
                    sibling_elements.click()
        time.sleep(Timer.FIVE_SECOND_TIMEOUT)

    def __is_required_fields_found(self):
        element_count = 0
        if self.card_holder_name_element:
            element_count = element_count + 1

        if self.card_number_element:
            element_count = element_count + 1
        
        if self.card_month_expiry_element:
            element_count = element_count + 1

        if self.card_year_expiry_element:
            element_count = element_count + 1

        if self.card_cvv_element:
            element_count = element_count + 1

        if element_count >= 3:
            return True
        return False

    def __scrap_required_elements(self):
        self.card_holder_name_element = self.__get_required_element(Pattern.CARD_HOLDER_NAME)
        self.card_number_element = self.__get_required_element(Pattern.CARD_NUMBER)
        self.card_month_expiry_element = self.__get_required_element(Pattern.EXPIRATION_MONTH)
        self.card_year_expiry_element = self.__get_required_element(Pattern.EXPIRATION_YEAR)
        self.card_cvv_element = self.__get_required_element(Pattern.CVV)

    def find_required_iframe(self):
        iframe_pattern = "//iframe[contains(translate(@title, 'PAYMENT', 'payment'), 'payment') " \
                         "or contains(translate(@title, 'CARDTINPU', 'cardtinpu'), 'card data input') " \
                         "or contains(translate(@id, 'IFRAMEXP', 'iframexp'), 'iframe-exp') " \
                         "or contains(translate(@id, 'IFRAMECN', 'iframecn'), 'iframe-ccn') " \
                         "or contains(translate(@id, 'IFRAMEXP', 'iframexp'), 'iframe-exp') " \
                         "or contains(translate(@id, 'IFRAMECV', 'iframecv'), 'iframe-cvv') " \
                         "or contains(translate(@id, 'CARDFIELDSNUMB', 'cardfieldsnumb'), 'card-fields-number') " \
                         "or contains(translate(@id, 'CARDFIELDSNM', 'cardfieldsnm'), 'card-fields-name') " \
                         "or contains(translate(@id, 'CARDFIELDSXPY', 'cardfieldsxpy'), 'card-fields-expiry') " \
                         "or contains(translate(@id, 'VERIFCATONALU', 'verifcatonalu'), 'verification_value')]"
        self.card_elements_iframes = self.web.finds_by_xpath_wait(iframe_pattern)
        if self.card_elements_iframes:
            self.is_card_details_found = True

    def focus_and_update_iframe_fields(self, card_number, card_holder_name, card_month_expiry, card_year_expiry,
                                       card_cvv, card_expiry, email):
         for iframe in self.card_elements_iframes:
            self.web.switch_to_frame(iframe)
            self.__scrap_required_elements()
            self.select_and_populate_card_details(card_number, card_holder_name, card_month_expiry, card_year_expiry,card_cvv, card_expiry, email)                                                  
            self.web.switch_to_default_content()

    def __extract_email_element(self):
        email_elements_dict = self.__extract_required_elements(Pattern.EMAIL, TagsList.POSSIBLE_INPUT_ELEMENT)
        if not email_elements_dict:
            return None
        return email_elements_dict['input'][0]

    def __extract_continue_elements(self, pattern):
        continue_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(continue_elements, TagsList.POSSIBLE_CONTINUE_BUTTON)

    def __extract_continue_button(self):
        continue_dict = self.__extract_continue_elements(Pattern.CONTINUE)
        if not continue_dict:
            return None
        return Utils.get_required_element_2(continue_dict, TagsList.POSSIBLE_CONTINUE_BUTTON)

    def __populate_email(self, email):
        try:
            self.email_element.send_keys(email)
            time.sleep(Timer.THREE_SECOND_TIMEOUT)
        except Exception as e:
            print(f"Exception while populating email {e}")

    def __continue(self):
        try:
            self.continue_button.click()
        except Exception as e:
            logging.info("In exception of card details continue button: ", str(e))