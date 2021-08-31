# Python Imports
import time

# Local Imports
from utility import constants
from modules.logger import logger
from utility.utilities import Utils


class Shipping:
    """
    This class is responsible to fill out shipping address details by identify
    shipping page type and other flows.
    """
    def __init__(self, context):
        self.context = context
        self.web = context.web
        self.web.open(self.context.url)
        time.sleep(16)

        self.first_name_element = None
        self.last_name_element = None
        self.email_element = None
        self.phone_country_code = None
        self.phone_element = None
        self.address1_element = None
        self.address2_element = None
        self.city_element = None
        self.state_element = None
        self.postal_code_element = None
        self.continue_elements = None

    def fill_out_data(self):
        """
        Taking every element 0 index is because no (input element exist more than 1)
        """
        logger.info("filling shipping data")
        self.first_name_element[0].send_keys("some Maaz")
        self.last_name_element[0].send_keys("some MaazMaazMaazMaaz")
        self.email_element[0].send_keys("maaz@gmail.com")
        if self.phone_country_code:
            self.phone_country_code[0].send_keys("92")
        self.phone_element[0].send_keys("17238912739")
        self.address1_element[0].send_keys("Home A1, 0th street, Houston.")
        if self.address2_element:
            self.address2_element[0].send_keys("Opposite to Alwa Bridge")
        self.city_element[0].send_keys("City")
        self.postal_code_element[0].send_keys("41015")

        all_options = self.state_element[0].find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") in ["MA", "USLA", "LA"]:
                option.click()

    def click_now(self):
        logger.info("clicking on done/continue button")
        continue_elements_dict = \
            Utils.fetch_required_elements(self.continue_elements, constants.Tags.POSSIBLE_CONTINUE_BUTTON)
        extracted_element_tag = Utils.get_required_tag(continue_elements_dict.keys(),
                                                       constants.Tags.POSSIBLE_CONTINUE_BUTTON)

        required_element = Utils.get_required_element(extracted_element_tag, continue_elements_dict)
        time.sleep(2)
        required_element.click()
        time.sleep(5)

    def fetching_required_elements(self):
        logger.info("fetching required elements")
        self.first_name_element = self.web.finds_by_xpath_wait(constants.Pattern.FIRST_NAME)
        self.last_name_element = self.web.finds_by_xpath_wait(constants.Pattern.LAST_NAME)
        self.email_element = self.web.finds_by_xpath_wait(constants.Pattern.EMAIL)
        self.phone_country_code = self.web.finds_by_xpath_wait(constants.Pattern.PREFIX)
        self.phone_element = self.web.finds_by_xpath_wait(constants.Pattern.PHONE)
        self.address1_element = self.web.finds_by_xpath_wait(constants.Pattern.ADDRESS1)
        self.address2_element = self.web.finds_by_xpath_wait(constants.Pattern.ADDRESS2)
        self.city_element = self.web.finds_by_xpath_wait(constants.Pattern.CITY)
        self.state_element = self.web.finds_by_xpath_wait(constants.Pattern.STATE)
        self.postal_code_element = self.web.finds_by_xpath_wait(constants.Pattern.POSTAL_CODE)
        self.continue_elements = self.web.finds_by_xpath_wait(constants.Pattern.CONTINUE)

    @staticmethod
    def identify_shipping_page_type():
        logger.info("Identifying shipping address page type")
        pass

    @staticmethod
    def fill_address_details():
        logger.info("Entering shipping address details.")
        pass
