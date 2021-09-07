# Framework imports
import time

from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException

# Local imports
from modules.logger import logger
from utility import constants
from utility.constants import Timer
from utility.user_personal_info import UserInfo


class ShipUtils:

    @staticmethod
    def get_country_code_element(country_elements):
        """ This function will return accurate element by matching country in 'name' attribute
        :param country_elements:
        :return:
        """
        for element in country_elements:
            if constants.UserInfo.COUNTRY in element.get_attribute(constants.ETC.NAME):
                return element

        return country_elements[0]

    @staticmethod
    def get_phone_element(phone_elements):
        """ This function will return accurate element by matching phone in the 'name' attribute
        :param phone_elements:
        :return:
        """
        for element in phone_elements:
            for val in ["number", "Number"]:
                if val in element.get_attribute(constants.ETC.NAME):
                    return element

        return phone_elements[0]

    @staticmethod
    def fill_name_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling name field")
        if len(shipping_info[constants.UserInfo.FULL_NAME]) > 0:
            try:
                time.sleep(Timer.ONE_SECOND_TIMEOUT)
                for element in shipping_info[constants.UserInfo.FULL_NAME]:
                    if element.is_enabled() and element.is_displayed() \
                            and not element.get_attribute(constants.ETC.VALUE):
                        element.send_keys(UserInfo.FULL_NAME)
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                logger.info(f"Exception Full Name: {str(e)}")

        if len(shipping_info[constants.UserInfo.FIRST_NAME]) > 0:
            try:
                time.sleep(Timer.ONE_SECOND_TIMEOUT)
                for element in shipping_info[constants.UserInfo.FIRST_NAME]:
                    if element.is_enabled() and element.is_displayed() \
                            and not element.get_attribute(constants.ETC.VALUE):
                        element.send_keys(UserInfo.FIRST_NAME)
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                logger.info(f"Exception First Name: {str(e)}")

        if len(shipping_info[constants.UserInfo.LAST_NAME]) > 0:
            try:
                time.sleep(Timer.ONE_SECOND_TIMEOUT)
                for element in shipping_info[constants.UserInfo.LAST_NAME]:
                    if element.is_enabled() and element.is_displayed() \
                            and not element.get_attribute(constants.ETC.VALUE):
                        element.send_keys(UserInfo.LAST_NAME)
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                logger.info(f"Exception Last Name: {str(e)}")

    @staticmethod
    def fill_email_field(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling email field")
        if not shipping_info[constants.UserInfo.EMAIL]:
            return

        # TODO Need to cross check this try except block as occurred in [gap.com]
        for element in shipping_info[constants.UserInfo.EMAIL]:
            try:
                if element.is_enabled() and element.is_displayed():
                    time.sleep(Timer.ONE_SECOND_TIMEOUT)
                    element.send_keys(UserInfo.EMAIL)
                    break
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                logger.info(f"Exception Email: {str(e)}")
                break

    @staticmethod
    def fill_phone_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling phone related fields")
        if shipping_info[constants.UserInfo.COUNTRY_CODE] and shipping_info[constants.UserInfo.PHONE]:
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            ShipUtils.get_country_code_element(shipping_info[constants.UserInfo.COUNTRY_CODE])\
                .send_keys(UserInfo.COUNTRY_CODE)
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            ShipUtils.get_phone_element(shipping_info[constants.UserInfo.PHONE])\
                .send_keys(UserInfo.PHONE)

        if shipping_info[constants.UserInfo.PHONE] and not shipping_info[constants.UserInfo.COUNTRY_CODE]:
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            shipping_info[constants.UserInfo.PHONE][0].send_keys("+"+UserInfo.PHONE)

    @staticmethod
    def fill_address_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling address related fields")
        if shipping_info[constants.UserInfo.ADDRESS1]:
            # shipping_info[constants.UserInfo.ADDRESS1][0].send_keys("Home A1, 0th street, Houston.")
            for element in shipping_info[constants.UserInfo.ADDRESS1]:
                try:
                    if element.is_enabled() and element.is_displayed():
                        time.sleep(Timer.ONE_SECOND_TIMEOUT)
                        element.send_keys(UserInfo.ADDRESS1)
                        break
                except Exception as e:
                    logger.info(f"Exception Address1: {str(e)}")
                    break

        if shipping_info[constants.UserInfo.ADDRESS2]:
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            shipping_info[constants.UserInfo.ADDRESS2][0].send_keys(UserInfo.ADDRESS2)

        if shipping_info[constants.UserInfo.CITY]:
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            shipping_info[constants.UserInfo.CITY][0].send_keys(UserInfo.CITY)

        if shipping_info[constants.UserInfo.POSTAL_CODE]:
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            shipping_info[constants.UserInfo.POSTAL_CODE][0].send_keys(UserInfo.POSTAL_CODE)

        ShipUtils.fill_state_attribute(shipping_info)

    @staticmethod
    def fill_state_attribute(shipping_info):
        """
        Filling state element with respect to its tag that can be [INPUT, SELECT]
        :param shipping_info:
        :return:
        """
        state_element = shipping_info[constants.UserInfo.STATE]
        if not state_element:
            return
        if state_element[0].tag_name == constants.Tags.INPUT:
            logger.info("Filling state using input")
            time.sleep(Timer.ONE_SECOND_TIMEOUT)
            state_element[0].send_keys(UserInfo.STATE_INPUT)
        else:
            logger.info("Filling state using select option")
            all_options = state_element[0].find_elements_by_tag_name(constants.ETC.OPTION)
            for option in all_options:
                if option.get_attribute(constants.ETC.VALUE) in UserInfo.STATE_OPTIONS:
                    option.click()
                    break
