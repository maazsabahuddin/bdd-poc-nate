#Local imports
import time
from utility.utilities import Utils
from utility.constants import Tags, Pattern

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
        print("\nemail elements: ", email_elements)
        first_name_elements = self.extract_required_elements(Pattern.FIRST_NAME)
        print("\nfirst_name elements: ", first_name_elements)
        last_name_elements = self.extract_required_elements(Pattern.LAST_NAME)
        print("\nlast_name elements: ", last_name_elements)
        phone_elements = self.extract_required_elements(Pattern.PHONE)
        print("\nphone elements: ", phone_elements)
        
        if not email_elements:
            print("\nemail element dict is not empty and it's length is: ", len(email_elements))
            if len(email_elements) > 1:
                self.email = Utils.get_required_element_related_to_guest(email_elements)
            else:
                print("\nemail element is: ", email_elements[0])
                self.email = email_elements[0]

        print("email element: ", self.email)
        
        if not first_name_elements:
            if len(first_name_elements) > 1:
                self.first_name = Utils.get_required_element('input', first_name_elements)
            else:
                self.first_name = first_name_elements[0]

        print("first name element: ", self.first_name)
        
        if not last_name_elements:
            if len(last_name_elements) > 1:
                self.last_name = Utils.get_required_element('input', last_name_elements)
            else:
                self.last_name = last_name_elements[0]

        print("last name element: ", self.last_name)
        
        if not phone_elements:
            if len(phone_elements) > 1:
                self.phone = Utils.get_required_element('input', phone_elements)
            else:
                self.phone = phone_elements[0]

        print("phone element: ", self.phone)
        
        if self.email or self.first_name or self.last_name or self.phone:
            self.is_required_field_found = True

    def extract_required_elements(self, pattern):
        required_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(required_elements, Tags.POSSIBLE_EMAIL_ELEMENT_LIST)['input']

    def fill_required_info(self, email=None, first_name=None, last_name=None, phone=None):
        if email is not None:
            self.email.send_keys(email)
        if first_name is not None:
            self.first_name.send_keys(first_name)
        if last_name is not None:
            self.last_name.send_keys(last_name)
        if phone is not None:
            self.phone.send_keys(phone)
        time.sleep(30)
