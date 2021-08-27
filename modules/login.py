# Python imports
import time

# Framework imports
from selenium.common import exceptions

# Local imports
from modules.constants import Tags, Pattern
from modules.utilities import Utils


class Login:

    def __init__(self, context):
        self.context = context
        self.web = context.web
        self.selected_login_guest_element = ""

    def find_login_as_guest_feature(self):
        """
        Main funtion which starts the searching process
        """
        login_as_guest_dict = self.fetch_login_as_guest_elements()
        if not login_as_guest_dict:
            self.context.found_login_as_guest = False
            return
        extracted_element_tag = Utils.get_required_tag(login_as_guest_dict.keys(), Tags.POSSIBLE_LOGIN_AS_GUEST_LIST)
        self.selected_login_guest_element = login_as_guest_dict[extracted_element_tag][0]
    
    def click_on_login_as_guest(self):
        """
        This function performs click on "Login as Guest" web element
        """
        try:
            self.selected_login_guest_element.click()
            # remove when run in production
            time.sleep(5)
        except (exceptions.StaleElementReferenceException, exceptions.ElementClickInterceptedException):
            print("Error in clicking login as guest button")

    def fetch_login_as_guest_elements(self):
        """
        This function returns dict containing elements which matches "login as guest" pattern
        """
        login_as_guest_elements = self.web.finds_by_xpath_wait(Pattern.LOGIN_AS_GUEST_PATTERN)
        return Utils.fetch_required_elements(login_as_guest_elements, Tags.POSSIBLE_LOGIN_AS_GUEST_LIST)
    
    def check_is_login_required(self):
        """
        This function checks if the current page requires login or we can continue without it
        """
        # fetch elements to check if its a checkout page having Checkout, Order Summary and Billing details
        is_checkout_elements = self.web.finds_by_xpath_wait(Pattern.IS_CHECKOUT_PAGE_PATTERN)
        elements_exist = [ele for ele in is_checkout_elements if ele.tag_name in Tags.POSSIBLE_CHECKOUT_PAGE_LIST]
        if elements_exist:
            # Then no need to require login, because we are on shipping details page
            self.context.is_login_required = False
            return
        else:
            # Search if login required
            login_elements = Utils.fetch_required_elements(Pattern.SIGN_IN_PATTERN, Tags.POSSIBLE_SIGNIN_LIST)
            if login_elements:
                # Do nothin as of now, because we have intially set context variable to true
                return
            else:
                # Here it comes means an unexpected page arose
                self.context.some_other_page = True 
                return
