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
        time.sleep(25)

        self.first_name_element = None
        self.last_name_element = None
        self.email_element = None
        self.phone_element = None
        self.address1_element = None
        self.address2_element = None
        self.city_element = None
        self.state_element = None
        self.postal_code_element = None
        self.continue_elements = None

    def fill_out_data(self):
        logger.info("filling shipping data")
        self.first_name_element.send_keys("some Maaz")
        self.last_name_element.send_keys("some MaazMaazMaazMaaz")
        self.email_element.send_keys("maaz@gmail.com")
        self.phone_element.send_keys("17238912739")
        self.address1_element.send_keys("Home A1, 0th street, Houston.")
        self.address2_element.send_keys("Opposite to Alwa Bridge")
        self.city_element.send_keys("City")
        self.postal_code_element.send_keys("41015")

        all_options = self.state_element.find_elements_by_tag_name("option")
        for option in all_options:
            if "LA" in option.get_attribute("value"):
                option.click()

    def click_now(self):
        logger.info("clicking on done/continue button")
        continue_elements_dict = \
            Utils.fetch_required_elements(self.continue_elements, constants.Tags.POSSIBLE_CONTINUE_BUTTON)
        extracted_element_tag = Utils.get_required_tag(continue_elements_dict.keys(),
                                                       constants.Tags.POSSIBLE_CONTINUE_BUTTON)
        required_element = Utils.get_required_element(extracted_element_tag, continue_elements_dict)
        required_element.click()

    def get_required_elements(self):
        logger.info("get required elements")
        self.first_name_element = self.web.find_by_xpath(constants.Pattern.FIRST_NAME)
        self.last_name_element = self.web.find_by_xpath(constants.Pattern.LAST_NAME)
        self.email_element = self.web.find_by_xpath(constants.Pattern.EMAIL)
        self.phone_element = self.web.find_by_xpath(constants.Pattern.PHONE)
        self.address1_element = self.web.find_by_xpath(constants.Pattern.ADDRESS1)
        self.address2_element = self.web.find_by_xpath(constants.Pattern.ADDRESS2)
        self.city_element = self.web.find_by_xpath(constants.Pattern.CITY)
        self.state_element = self.web.find_by_xpath(constants.Pattern.STATE)
        self.postal_code_element = self.web.find_by_xpath(constants.Pattern.POSTAL_CODE)
        self.continue_elements = self.web.finds_by_xpath_wait(constants.Pattern.CONTINUE)

    @staticmethod
    def identify_shipping_page_type():
        logger.info("Identifying shipping address page type")
        pass

    @staticmethod
    def fill_address_details():
        logger.info("Entering shipping address details.")
        pass
