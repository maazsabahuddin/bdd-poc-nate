#Local imports
import time
from utility.utilities import Utils
from utility.constants import Tags, Pattern, Timer

class PersonalInfo:
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.email = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.is_required_field_found = False

    def find_personal_info_elements(self):
        email_elements = self.extract_required_elements(Pattern.EMAIL)
        first_name_elements = self.extract_required_elements(Pattern.FIRST_NAME)
        last_name_elements = self.extract_required_elements(Pattern.LAST_NAME)
        phone_elements = self.extract_required_elements(Pattern.PHONE)
        
        if email_elements:
            if len(email_elements) > 1:
                self.email = Utils.get_required_element_related_to_guest('input', email_elements)
            else:
                self.email = email_elements['input'][0]

        if first_name_elements:
            if len(first_name_elements) > 1:
                self.first_name = Utils.get_required_element('input', first_name_elements)
            else:
                self.first_name = first_name_elements['input'][0]
        
        if last_name_elements:
            if len(last_name_elements) > 1:
                self.last_name = Utils.get_required_element('input', last_name_elements)
            else:
                self.last_name = last_name_elements['input'][0]
        
        if phone_elements:
            if len(phone_elements) > 1:
                self.phone = Utils.get_required_element('input', phone_elements)
            else:
                self.phone = phone_elements['input'][0]
        
        if self.email or self.first_name or self.last_name or self.phone:
            self.is_required_field_found = True
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def extract_required_elements(self, pattern):
        required_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(required_elements, Tags.POSSIBLE_EMAIL_ELEMENT_LIST)

    def fill_required_info(self, email, first_name, last_name, phone):
        if email is not None:
            self.email.send_keys(email)
        if first_name is not None:
            self.first_name.send_keys(first_name)
        if last_name is not None:
            self.last_name.send_keys(last_name)
        if phone is not None:
            self.phone.send_keys(phone)
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
