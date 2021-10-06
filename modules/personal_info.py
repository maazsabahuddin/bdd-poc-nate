# Python imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from modules.logger import logger
from utility.ship_utils import ShipUtils
from utility.utilities import Utils
from utility.constants import TagsList, Pattern, Timer


class PersonalInfo:

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.email = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.button = None
        self.is_required_field_found = False
        self.is_data_populated = False

    def find_personal_info_elements(self):
        email_elements_dict = self.extract_required_elements(Pattern.EMAIL, TagsList.POSSIBLE_INPUT_ELEMENT)
        first_name_elements_dict = self.extract_required_elements(Pattern.FIRST_NAME, TagsList.POSSIBLE_INPUT_ELEMENT)
        last_name_elements_dict = self.extract_required_elements(Pattern.LAST_NAME, TagsList.POSSIBLE_INPUT_ELEMENT)
        phone_elements_dict = self.extract_required_elements(Pattern.PHONE, TagsList.POSSIBLE_INPUT_ELEMENT)
        button_elements_dict = self.extract_required_elements(Pattern.GUEST_BUTTON,
                                                              TagsList.POSSIBLE_LOGIN_AS_GUEST_LIST)
        
        if email_elements_dict:
            if len(email_elements_dict['input']) > 1:
                self.email = Utils.get_required_element_related_to_guest('input', email_elements_dict)
            else:
                self.email = email_elements_dict['input'][0]

        if first_name_elements_dict:
            if len(first_name_elements_dict['input']) > 1:
                self.first_name = Utils.get_required_element('input', first_name_elements_dict)
            else:
                self.first_name = first_name_elements_dict['input'][0]
        
        if last_name_elements_dict:
            if len(last_name_elements_dict['input']) > 1:
                self.last_name = Utils.get_required_element('input', last_name_elements_dict)
            else:
                self.last_name = last_name_elements_dict['input'][0]
        
        if phone_elements_dict:
            if len(phone_elements_dict['input']) > 1:
                phone_element = Utils.get_required_element('input', phone_elements_dict)
                if phone_element:
                    self.phone = phone_element if ShipUtils.validate_phone_element(phone_element) else None
                else:
                    self.phone = None
            else:
                self.phone = phone_elements_dict['input'][0] \
                    if ShipUtils.validate_phone_element(phone_elements_dict['input'][0]) else None
        
        if button_elements_dict:
            element_key = "a"
            if 'button' in button_elements_dict:
                element_key = 'button'
            if len(button_elements_dict[element_key]) > 1:
                self.button = Utils.get_required_element_related_to_guest(element_key, button_elements_dict)
            else:
                self.button = button_elements_dict[element_key][0]
        
        if self.email or self.first_name or self.last_name or self.phone:
            self.is_required_field_found = True
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def extract_required_elements(self, pattern, posible_elements_list):
        required_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(required_elements, posible_elements_list)

    def fill_required_info(self, email, first_name, last_name, phone):
        if email is not None:
            self.email.send_keys(email)
            self.is_data_populated = True
        if first_name is not None:
            self.first_name.send_keys(first_name)
            self.is_data_populated = True
        if last_name is not None:
            self.last_name.send_keys(last_name)
            self.is_data_populated = True
        if phone is not None:
            self.phone.send_keys(phone)
            self.is_data_populated = True
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
    
    def hit_to_proceed(self):
        if self.button is not None:
            try:
                self.button.click()
                time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
            except exceptions.ElementNotInteractableException as e:
                logger.info(f"\nPersonal info {str(e)}")
