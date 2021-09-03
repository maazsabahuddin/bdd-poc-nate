# Python Imports
import time
import os

# Local Imports
from utility import constants
from modules.logger import logger
from utility.constants import Timer
from utility.ship_utils import ShipUtils
from utility.utilities import Utils


class Shipping:
    """
    This class is responsible to fill out shipping address details by identify
    shipping page type and other flows.
    """
    def __init__(self, context):
        self.context = context
        self.web = context.web

        logger.info("Initializing shipping address variables.")
        self.shipping_info = {}

        logger.info("Initializing shipping required elements with respect to the flow.")
        self.variable_flow_required_elements = [constants.UserInfo.ADDRESS1, constants.UserInfo.STATE,
                                                constants.UserInfo.POSTAL_CODE, constants.UserInfo.CITY,
                                                constants.UserInfo.CONTINUE]
        self.direct_flow_required_elements = [constants.UserInfo.FIRST_NAME, constants.UserInfo.LAST_NAME,
                                              constants.UserInfo.EMAIL, constants.UserInfo.PHONE,
                                              constants.UserInfo.ADDRESS1, constants.UserInfo.STATE,
                                              constants.UserInfo.CONTINUE, constants.UserInfo.POSTAL_CODE,
                                              constants.UserInfo.CITY]
        self.login_flow_required_elements = [constants.UserInfo.FULL_NAME, constants.UserInfo.ADDRESS1,
                                             constants.UserInfo.STATE, constants.UserInfo.CONTINUE,
                                             constants.UserInfo.POSTAL_CODE, constants.UserInfo.CITY,
                                             constants.UserInfo.PHONE]
        self.after_personal_information_flow_required_elements = [constants.UserInfo.ADDRESS1, constants.UserInfo.STATE,
                                                                  constants.UserInfo.POSTAL_CODE,
                                                                  constants.UserInfo.CITY, constants.UserInfo.CONTINUE]
        self.login_flow = False
        self.personal_information_flow = False
        self.direct_flow = False
        self.variable_flow = True

    @staticmethod
    def fill_variable_flow_data(shipping_info):
        """
        This function is responsible to fill out all the related to variable flow
        :param shipping_info:
        :return:
        """
        ShipUtils.fill_name_related_fields(shipping_info)
        ShipUtils.fill_email_field(shipping_info)
        ShipUtils.fill_phone_related_fields(shipping_info)
        ShipUtils.fill_address_related_fields(shipping_info)

    @staticmethod
    def fill_direct_flow_data(shipping_info):
        """
        This function is responsible to fill out all the related to direct flow
        :param shipping_info:
        :return:
        """
        ShipUtils.fill_name_related_fields(shipping_info)
        ShipUtils.fill_email_field(shipping_info)
        ShipUtils.fill_phone_related_fields(shipping_info)
        ShipUtils.fill_address_related_fields(shipping_info)

    @staticmethod
    def fill_login_flow_data(shipping_info):
        """
        This function is responsible to fill out all the related to login flow
        :param shipping_info:
        :return:
        """
        ShipUtils.fill_name_related_fields(shipping_info)
        ShipUtils.fill_phone_related_fields(shipping_info)
        ShipUtils.fill_address_related_fields(shipping_info)

    @staticmethod
    def fill_after_personal_flow_data(shipping_info):
        """
        This function is responsible to fill out all the related to personal flow
        :param shipping_info:
        :return:
        """
        ShipUtils.fill_name_related_fields(shipping_info)
        ShipUtils.fill_phone_related_fields(shipping_info)
        ShipUtils.fill_address_related_fields(shipping_info)

    def fill_out_data(self):
        """
        Taking every element 0 index is because no (input element exist more than 1)
        """
        logger.info("filling shipping data")
        if self.variable_flow:
            logger.info("filling login flow shipping data")
            self.fill_variable_flow_data(self.shipping_info)
        elif self.direct_flow:
            logger.info("filling direct flow shipping data")
            self.fill_direct_flow_data(self.shipping_info)
        elif self.login_flow:
            logger.info("filling variable flow shipping data")
            self.fill_login_flow_data(self.shipping_info)
        else:
            logger.info("filling personal flow shipping data")
            self.fill_after_personal_flow_data(self.shipping_info)

        if self.shipping_info[constants.UserInfo.CONSENT]:
            # TODO Have to click this consent in order to move forwards (NIKE)
            pass

    def click_now(self):
        logger.info("clicking on done/continue button")
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        continue_elements_dict = \
            Utils.fetch_required_elements(self.shipping_info[constants.UserInfo.CONTINUE],
                                          constants.Tags.POSSIBLE_CONTINUE_BUTTON)
        if not continue_elements_dict:
            logger.info("Button element not found.")
            logger.info("Aborting..")
            os.abort()

        extracted_element_tag = Utils.get_required_tag(continue_elements_dict.keys(),
                                                       constants.Tags.POSSIBLE_CONTINUE_BUTTON)
        required_element = Utils.get_required_element(extracted_element_tag, continue_elements_dict)
        if not required_element:
            logger.info(f"{extracted_element_tag} element is not clickable")
            os.abort()

        required_element.click()
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def get_validation_keys(self):
        """
        This function is responsible to return all the required elements on the basis of flow execution
        :param self:
        :return:
        """
        if self.variable_flow:
            logger.info("Variable flow execution")
            return {key: self.shipping_info.get(key) for key in self.variable_flow_required_elements
                    if self.shipping_info.get(key) != []}

        elif self.direct_flow:
            logger.info("Direct flow execution")
            return {key: self.shipping_info.get(key) for key in self.direct_flow_required_elements
                    if self.shipping_info.get(key) != []}
        elif self.login_flow:
            logger.info("Login flow execution")
            return {key: self.shipping_info.get(key) for key in self.login_flow_required_elements
                    if self.shipping_info.get(key) != []}

        logger.info("Personal information flow execution")
        return {key: self.shipping_info.get(key) for key in self.after_personal_information_flow_required_elements
                if self.shipping_info.get(key) != []}

    def validate_fields(self):
        """
        Validating all the required fields if any of them are not fetched abort the program.
        """
        logger.info("Validating fields..")
        validated_keys = self.get_validation_keys()

        required_element_keys = set(self.direct_flow_required_elements) if self.direct_flow \
            else set(self.after_personal_information_flow_required_elements) if self.personal_information_flow \
            else set(self.login_flow_required_elements) if self.login_flow \
            else set(self.variable_flow_required_elements)

        logger.info(f"Validated keys: {set(validated_keys)}")
        logger.info(f"Required keys: {required_element_keys}")

        if set(validated_keys) != set(required_element_keys):
            logger.info(f"Cannot fetched some of the required elements "
                        f"{required_element_keys - set(validated_keys)}")
            logger.info("Not Aborting..")
            logger.info("Continue the flow")
            return True

        logger.info("Data Validated..")
        return True

    def fetching_required_elements(self):
        logger.info("fetching required elements")
        self.shipping_info[constants.UserInfo.FIRST_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.FIRST_NAME)
        self.shipping_info[constants.UserInfo.LAST_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.LAST_NAME)
        self.shipping_info[constants.UserInfo.FULL_NAME] = self.web.finds_by_xpath_wait(constants.Pattern.FULL_NAME)
        self.shipping_info[constants.UserInfo.EMAIL] = self.web.finds_by_xpath_wait(constants.Pattern.EMAIL)
        self.shipping_info[constants.UserInfo.COUNTRY_CODE] = \
            self.web.finds_by_xpath_wait(constants.Pattern.COUNTRY_CODE)
        self.shipping_info[constants.UserInfo.PHONE] = self.web.finds_by_xpath_wait(constants.Pattern.PHONE)
        self.shipping_info[constants.UserInfo.ADDRESS1] = self.web.finds_by_xpath_wait(constants.Pattern.ADDRESS1)
        self.shipping_info[constants.UserInfo.ADDRESS2] = self.web.finds_by_xpath_wait(constants.Pattern.ADDRESS2)
        self.shipping_info[constants.UserInfo.CITY] = self.web.finds_by_xpath_wait(constants.Pattern.CITY)
        self.shipping_info[constants.UserInfo.STATE] = self.web.finds_by_xpath_wait(constants.Pattern.STATE)
        self.shipping_info[constants.UserInfo.POSTAL_CODE] = self.web.finds_by_xpath_wait(constants.Pattern.POSTAL_CODE)
        self.shipping_info[constants.UserInfo.CONTINUE] = self.web.finds_by_xpath_wait(constants.Pattern.CONTINUE)
        self.shipping_info[constants.UserInfo.CONSENT] = self.web.finds_by_xpath_wait(constants.Pattern.CONSENT)

        logger.info("Fetched")
        logger.info(f"DATA FOUND: {self.shipping_info}")
