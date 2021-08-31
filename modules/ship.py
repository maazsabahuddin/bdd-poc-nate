# Python Imports
import time
import os

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
        time.sleep(3)

        logger.info("Initializing shipping address variables.")
        self.shipping_info = {}
        self.required_elements = [constants.ETC.FIRST_NAME, constants.ETC.LAST_NAME, constants.ETC.EMAIL,
                                  constants.ETC.PHONE, constants.ETC.ADDRESS1, constants.ETC.STATE,
                                  constants.ETC.CONTINUE, constants.ETC.POSTAL_CODE, constants.ETC.CITY]

    def fill_out_data(self):
        """
        Taking every element 0 index is because no (input element exist more than 1)
        """
        logger.info("filling shipping data")
        self.shipping_info[constants.ETC.FIRST_NAME][0].send_keys("Maaz")
        self.shipping_info[constants.ETC.LAST_NAME][0].send_keys("Sabah Uddin")
        self.shipping_info[constants.ETC.EMAIL][0].send_keys("maaz@gmail.com")
        if self.shipping_info[constants.ETC.COUNTRY_CODE]:
            self.shipping_info[constants.ETC.COUNTRY_CODE][0].send_keys("92")
            self.shipping_info[constants.ETC.PHONE][0].send_keys("6473479480")
        if self.shipping_info[constants.ETC.PHONE] and not self.shipping_info[constants.ETC.COUNTRY_CODE]:
            self.shipping_info[constants.ETC.PHONE][0].send_keys("6473479480")
        self.shipping_info[constants.ETC.ADDRESS1][0].send_keys("Home A1, 0th street, Houston.")
        if self.shipping_info[constants.ETC.ADDRESS2]:
            self.shipping_info[constants.ETC.ADDRESS2][0].send_keys("Opposite to Alwa Bridge")
        self.shipping_info[constants.ETC.CITY][0].send_keys("City")
        self.shipping_info[constants.ETC.POSTAL_CODE][0].send_keys("a2s2s2")

        all_options = self.shipping_info[constants.ETC.STATE][0].find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") in ["MA", "USLA", "LA", "AL"]:
                option.click()

        if self.shipping_info[constants.ETC.CONSENT]:
            # TODO Have to click this consent in order to move forwards (NIKE)
            pass

    def click_now(self):
        logger.info("clicking on done/continue button")
        continue_elements_dict = \
            Utils.fetch_required_elements(self.shipping_info[constants.ETC.CONTINUE],
                                          constants.Tags.POSSIBLE_CONTINUE_BUTTON)
        if not continue_elements_dict:
            logger.info("Button not found.")
            logger.info("Aborting")
            os.abort()

        extracted_element_tag = Utils.get_required_tag(continue_elements_dict.keys(),
                                                       constants.Tags.POSSIBLE_CONTINUE_BUTTON)

        required_element = Utils.get_required_element(extracted_element_tag, continue_elements_dict)
        required_element.click()
        time.sleep(5)

    def validate_fields(self):
        """
        Validating all the required fields if any of them are not fetched abort the program.
        """
        logger.info("Validating fields..")
        validated_keys = {key: self.shipping_info.get(key) for key in self.required_elements
                          if self.shipping_info.get(key) != []}

        logger.info(f"Validated keys: {set(validated_keys)}")
        logger.info(f"Required keys: {set(self.required_elements)}")

        if set(validated_keys) != set(self.required_elements):
            logger.info(f"Cannot fetched some of the required elements "
                        f"{set(self.required_elements) - set(validated_keys)}")
            logger.info("Aborting..")
            os.abort()

    def fetching_required_elements(self):
        logger.info("fetching required elements")
        self.shipping_info[constants.ETC.FIRST_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.FIRST_NAME)
        self.shipping_info[constants.ETC.LAST_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.LAST_NAME)
        self.shipping_info[constants.ETC.EMAIL] = self.web.finds_by_xpath_wait(constants.Pattern.EMAIL)
        self.shipping_info[constants.ETC.COUNTRY_CODE] = self.web.finds_by_xpath_wait(constants.Pattern.COUNTRY_CODE)
        self.shipping_info[constants.ETC.PHONE] = self.web.finds_by_xpath_wait(constants.Pattern.PHONE)
        self.shipping_info[constants.ETC.ADDRESS1] = self.web.finds_by_xpath_wait(constants.Pattern.ADDRESS1)
        self.shipping_info[constants.ETC.ADDRESS2] = self.web.finds_by_xpath_wait(constants.Pattern.ADDRESS2)
        self.shipping_info[constants.ETC.CITY] = self.web.finds_by_xpath_wait(constants.Pattern.CITY)
        self.shipping_info[constants.ETC.STATE] = self.web.finds_by_xpath_wait(constants.Pattern.STATE)
        self.shipping_info[constants.ETC.POSTAL_CODE] = self.web.finds_by_xpath_wait(constants.Pattern.POSTAL_CODE)
        self.shipping_info[constants.ETC.CONTINUE] = self.web.finds_by_xpath_wait(constants.Pattern.CONTINUE)
        self.shipping_info[constants.ETC.CONSENT] = self.web.finds_by_xpath_wait(constants.Pattern.CONSENT)

        logger.info("Fetched")
        self.validate_fields()

    @staticmethod
    def identify_shipping_page_type():
        logger.info("Identifying shipping address page type")
        pass

    @staticmethod
    def fill_address_details():
        logger.info("Entering shipping address details.")
        pass
