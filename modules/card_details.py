# Python imports
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
        
    def find_card_details_elements(self):
        time.sleep(120)
        # time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        print("start extracting elements")
        
        self.__update_card_type_details_if_any(Pattern.CARD_TYPE)
        self.__scrap_required_elements()
        self.is_card_details_found = self.__is_required_fields_found()
        if not self.is_card_details_found:
            print("finding for iframe")
            self.find_required_iframe()

    def __get_required_element(self, pattern):
        extracted_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.extract_required_element_2(list_of_elements=extracted_elements)
    
    def select_and_populate_card_details(self, card_number, card_holder_name, 
        card_month_expiry, card_year_expiry, card_cvv, card_expiry):
        if self.card_number_element:
            self.__populate_card_number(number=card_number)
        if self.card_month_expiry_element:
            self.__populate_card_expiration_details(month=card_month_expiry, year=card_year_expiry, m_y=card_expiry)
        if self.card_holder_name_element:
            self.__populate_card_holder_name(name=card_holder_name)
        if self.card_cvv_element:
            self.__populate_card_security_code(cvv=card_cvv)
        time.sleep(15)

    def __populate_month(self, month):
        if self.card_month_expiry_element.tag_name == Tags.SELECT:
            all_options = self.card_month_expiry_element.find_elements_by_tag_name(ETC.OPTION)
            for option in all_options:
                if option.get_attribute(ETC.VALUE) == UserInfo.CARD_EXPIRATION_MONTH:
                    option.click()
                    break
        else:
            self.card_month_expiry_element.send_keys(month)
        time.sleep(Timer.ONE_SECOND_TIMEOUT)

    def __populate_year(self, year):
        if self.card_year_expiry_element.tag_name == Tags.SELECT:
            all_options = self.card_year_expiry_element.find_elements_by_tag_name(ETC.OPTION)
            for option in all_options:
                if option.get_attribute(ETC.VALUE) == UserInfo.CARD_EXPIRATION_YEAR:
                    option.click()
                    break
        else:
            self.card_month_expiry_element.send_keys(year)
        time.sleep(Timer.ONE_SECOND_TIMEOUT)

    def __populate_card_holder_name(self, name):
        if self.card_holder_name_element != None:
            self.card_holder_name_element.send_keys(name)
            time.sleep(Timer.ONE_SECOND_TIMEOUT)

    def __populate_card_expiration_details(self, month, year, m_y):
        if self.card_year_expiry_element:
            self.__populate_month(month=month)
            self.__populate_year(year=year)
        else:
            self.__populate_month(month=m_y)

    def __populate_card_number(self, number):
        self.card_number_element.send_keys(number)
        time.sleep(Timer.ONE_SECOND_TIMEOUT)

    def __populate_card_security_code(self, cvv):
        self.card_cvv_element.send_keys(cvv)
        time.sleep(Timer.ONE_SECOND_TIMEOUT)

    def __update_card_type_details_if_any(self, pattern):
        extracted_elements = self.web.finds_by_xpath_wait(pattern)
        print("extracted elements: ", extracted_elements)
        card_type_dict = Utils.fetch_required_elements3(extracted_elements, TagsList.POSSIBLE_CARD_TYPE_ELEMENTS)
        print("card type dictionary: ", card_type_dict)
        card_type_element = Utils.get_required_element_2(card_type_dict, TagsList.POSSIBLE_CARD_TYPE_ELEMENTS)
        self.__select_card_type(element=card_type_element)

    def __select_card_type(self, element):
        if element:
            if element.tag_name == Tags.SELECT:
                all_options = element.find_elements_by_tag_name(ETC.OPTION)
                for option in all_options:
                    if option.get_attribute(ETC.TEXT) in UserInfo.CARD_TYPE:
                        option.click()
                        break
            else:
                print("trying to click on different element")
                print(element.get_attribute("outerHTML"))
                try:
                    element.click()
                except exceptions.ElementNotInteractableException:
                    print("In exception")
                    parent_element = Utils.find_parent_element_from_child(child_element=element, filter_list=["label"])
                    if parent_element:
                        print("parent clicked")
                        parent_element.click()
                    else:
                        print("finding label using for attribute")
                        element_id = element.get_attribute("id")
                        print("element id: ", element_id)
                        sibling_elements = self.web.find_by_xpath(f"//label[@for={element_id}]")
                        if sibling_elements:
                            print("clicking on sibling")
                            sibling_elements.click()
                        else:
                            return
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

    def __scrap_required_elements(self):
        self.card_holder_name_element = self.__get_required_element(Pattern.CARD_HOLDER_NAME)
        self.card_number_element = self.__get_required_element(Pattern.CARD_NUMBER)
        print("card number: ", self.card_number_element)
        self.card_month_expiry_element = self.__get_required_element(Pattern.EXPIRATION_MONTH)
        print("card expiry month: ", self.card_month_expiry_element)
        self.card_year_expiry_element = self.__get_required_element(Pattern.EXPIRATION_YEAR)
        self.card_cvv_element = self.__get_required_element(Pattern.CVV)
        print("card cvv: ", self.card_cvv_element)

    def find_required_iframe(self):
        iframe_pattern = "//iframe[contains(translate(@title, 'PAYMENT', 'payment'), 'payment') " \
                         "or contains(translate(@title, 'CARDTINPU', 'cardtinpu'), 'card data input') " \
                         "or contains(translate(@id, 'IFRAMEXP', 'iframexp'), 'iframe-exp') " \
                         "or contains(translate(@id, 'IFRAMECN', 'iframecn'), 'iframe-ccn') " \
                         "or contains(translate(@id, 'IFRAMEXP', 'iframexp'), 'iframe-exp') " \
                         "or contains(translate(@id, 'IFRAMECV', 'iframecv'), 'iframe-cvv')]"
        self.card_elements_iframes = self.web.finds_by_xpath_wait(iframe_pattern)
        if self.card_elements_iframes:
            self.is_card_details_found = True

    def focus_and_update_iframe_fields(self, card_number, card_holder_name, 
        card_month_expiry, card_year_expiry, card_cvv, card_expiry):
        for iframe in self.card_elements_iframes:
            self.web.switch_to_frame(iframe)
            self.__scrap_required_elements()
            self.select_and_populate_card_details(card_number, card_holder_name, 
                card_month_expiry, card_year_expiry, card_cvv, card_expiry)
            self.web.switch_to_default_content()