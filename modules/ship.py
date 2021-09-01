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

        logger.info("Initializing shipping required elements with respect to the flow.")
        self.direct_flow_required_elements = [constants.ETC.FIRST_NAME, constants.ETC.LAST_NAME, constants.ETC.EMAIL,
                                              constants.ETC.PHONE, constants.ETC.ADDRESS1, constants.ETC.STATE,
                                              constants.ETC.CONTINUE, constants.ETC.POSTAL_CODE, constants.ETC.CITY]
        self.login_flow_required_elements = [constants.ETC.FULL_NAME, constants.ETC.ADDRESS1, constants.ETC.STATE,
                                             constants.ETC.CONTINUE, constants.ETC.POSTAL_CODE, constants.ETC.CITY,
                                             constants.ETC.PHONE]
        self.personal_information_flow_required_elements = [constants.ETC.FIRST_NAME, constants.ETC.LAST_NAME,
                                                            constants.ETC.PHONE, constants.ETC.ADDRESS1,
                                                            constants.ETC.STATE, constants.ETC.CONTINUE,
                                                            constants.ETC.POSTAL_CODE, constants.ETC.CITY]
        self.login_flow = False
        self.personal_information_flow = False
        self.direct_flow = False

    def fill_state_attribute(self):
        """
        Filling state element with respect to its tag that can be [INPUT, SELECT]
        """
        state_element = self.shipping_info[constants.ETC.STATE][0]
        if state_element.tag_name == constants.Tags.INPUT:
            logger.info("Filling state using input")
            state_element.send_keys("Ontario")
        else:
            logger.info("Filling state using select option")
            all_options = state_element.find_elements_by_tag_name("option")
            for option in all_options:
                if option.get_attribute("value") in ["MA", "USLA", "LA", "AL"]:
                    option.click()

    def fill_out_data(self):
        """
        Taking every element 0 index is because no (input element exist more than 1)
        """
        logger.info("filling shipping data")
        if self.login_flow:
            self.shipping_info[constants.ETC.FULL_NAME][0].send_keys("Maaz Sabah Uddin")

        if not self.login_flow:
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

        self.fill_state_attribute()

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

    def get_validation_keys(self):
        """
        This function is responsible to return all the required elements on the basis of flow execution
        :param self:
        :return:
        """
        if self.direct_flow:
            logger.info("Direct flow execution")
            return {key: self.shipping_info.get(key) for key in self.direct_flow_required_elements
                    if self.shipping_info.get(key) != []}
        elif self.login_flow:
            logger.info("Login flow execution")
            return {key: self.shipping_info.get(key) for key in self.login_flow_required_elements
                    if self.shipping_info.get(key) != []}

        logger.info("Personal information flow execution")
        return {key: self.shipping_info.get(key) for key in self.personal_information_flow_required_elements
                if self.shipping_info.get(key) != []}

    def validate_fields(self):
        """
        Validating all the required fields if any of them are not fetched abort the program.
        """
        logger.info("Validating fields..")
        validated_keys = self.get_validation_keys()

        required_element_keys = set(self.direct_flow_required_elements) if self.direct_flow \
            else set(self.login_flow_required_elements)

        logger.info(f"Validated keys: {set(validated_keys)}")
        logger.info(f"Required keys: {required_element_keys}")

        if set(validated_keys) != set(required_element_keys):
            logger.info(f"Cannot fetched some of the required elements "
                        f"{required_element_keys - set(validated_keys)}")
            logger.info("Aborting..")
            os.abort()

        logger.info("Data Validated..")

    def fetching_required_elements(self):
        logger.info("fetching required elements")
        self.shipping_info[constants.ETC.FIRST_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.FIRST_NAME)
        self.shipping_info[constants.ETC.LAST_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.LAST_NAME)
        self.shipping_info[constants.ETC.FULL_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.FULL_NAME)
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
