# Python imports
# import time

# Framework imports
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException

# Local imports
from modules.logger import logger
from utility import constants
# from utility.constants import Timer
from utility.user_personal_info import UserInfo


class ShipUtils:

    @staticmethod
    def validate_address_element(element):
        for val in ["firstName", "firstname", "lastName", "lastname", "state", "city", "postalCode"]:
            if val in element.get_attribute(constants.ETC.NAME):
                return False
        return True

    @staticmethod
    def get_country_code_element(country_elements):
        """ This function will return accurate element by matching country in 'name' attribute
        :param country_elements:
        :return:
        """
        for element in country_elements:
            if constants.UserInfo.COUNTRY in element.get_attribute(constants.ETC.NAME) and \
                    element.is_enabled() and element.is_displayed():
                return element

    @staticmethod
    def get_phone_element(phone_elements):
        """ This function will return accurate element by matching phone in the 'name' attribute
        :param phone_elements:
        :return:
        """
        for element in phone_elements:
            for val in ["number", "Number"]:
                if val in element.get_attribute(constants.ETC.NAME) and \
                        element.is_enabled() and element.is_displayed():
                    return element

    @staticmethod
    def fill_country_field(shipping_info):
        logger.info("Filling country field")
        country_element = shipping_info[constants.UserInfo.COUNTRY]
        if not country_element:
            return

        for element in country_element:
            if not element.is_enabled() or not element.is_displayed():
                continue
            all_options = element.find_elements_by_tag_name(constants.ETC.OPTION)
            for option in all_options:
                if option.get_attribute(constants.ETC.VALUE) in UserInfo.COUNTRY_OPTIONS:
                    option.click()
                    break

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
                # time.sleep(Timer.ONE_SECOND_TIMEOUT)
                for element in shipping_info[constants.UserInfo.FULL_NAME]:
                    if element.is_enabled() and element.is_displayed() \
                            and not element.get_attribute(constants.ETC.VALUE):
                        element.send_keys(UserInfo.FULL_NAME)
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                logger.info(f"Exception Full Name: {str(e)}")

        if len(shipping_info[constants.UserInfo.FIRST_NAME]) > 0:
            try:
                # time.sleep(Timer.ONE_SECOND_TIMEOUT)
                for element in shipping_info[constants.UserInfo.FIRST_NAME]:
                    if element.is_enabled() and element.is_displayed() \
                            and not element.get_attribute(constants.ETC.VALUE):
                        element.send_keys(UserInfo.FIRST_NAME)
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                logger.info(f"Exception First Name: {str(e)}")

        if len(shipping_info[constants.UserInfo.LAST_NAME]) > 0:
            try:
                # time.sleep(Timer.ONE_SECOND_TIMEOUT)
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
                if element.is_enabled() and element.is_displayed() and not element.get_attribute(constants.ETC.VALUE):
                    # time.sleep(Timer.ONE_SECOND_TIMEOUT)
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
        # If Phone number and country code both are present then this condition will be true.
        if shipping_info[constants.UserInfo.COUNTRY_CODE] and shipping_info[constants.UserInfo.PHONE]:

            country_element = ShipUtils.get_country_code_element(shipping_info[constants.UserInfo.COUNTRY_CODE])
            if country_element:
                # time.sleep(Timer.ONE_SECOND_TIMEOUT)
                country_element.send_keys(UserInfo.COUNTRY_CODE)

            phone_element = ShipUtils.get_phone_element(shipping_info[constants.UserInfo.PHONE])
            if phone_element and not phone_element.get_attribute(constants.ETC.VALUE):
                phone_element.send_keys(UserInfo.PHONE)

        # If Phone number is present but country code is not present then this condition will be true.
        elif shipping_info[constants.UserInfo.PHONE] and not shipping_info[constants.UserInfo.COUNTRY_CODE]:

            phone_element = ShipUtils.get_phone_element(shipping_info[constants.UserInfo.PHONE])
            if not phone_element:
                return

            # If the phone element is not prefilled then this condition will be true
            if phone_element.get_attribute(constants.ETC.VALUE):
                # time.sleep(Timer.ONE_SECOND_TIMEOUT)
                phone_element.send_keys(f"+{UserInfo.PHONE}")

            # If the phone element is prefilled with + sign then this condition will be true
            elif phone_element.get_attribute(constants.ETC.VALUE)[0] == "+":
                # time.sleep(Timer.ONE_SECOND_TIMEOUT)
                phone_element.send_keys(UserInfo.PHONE)

    @staticmethod
    def fill_address_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling address related fields")
        for element in shipping_info[constants.UserInfo.ADDRESS1]:
            try:
                if element.is_enabled() and element.is_displayed() and ShipUtils.validate_address_element(element):
                    # time.sleep(Timer.ONE_SECOND_TIMEOUT)
                    element.send_keys(UserInfo.ADDRESS1)
                    break
            except Exception as e:
                logger.info(f"Exception Address1: {str(e)}")
                break

        address2_elements = shipping_info[constants.UserInfo.ADDRESS2]
        if address2_elements:
            # time.sleep(Timer.ONE_SECOND_TIMEOUT)
            for element in address2_elements:
                if not element.is_enabled() or not element.is_displayed():
                    continue
                element.send_keys(UserInfo.ADDRESS2)

        city_elements = shipping_info[constants.UserInfo.CITY]
        for element in city_elements:
            if not element.is_enabled() or not element.is_displayed():
                continue
            if element.get_attribute(constants.ETC.VALUE):
                element.clear()
            # time.sleep(Timer.ONE_SECOND_TIMEOUT)
            element.send_keys(UserInfo.CITY)

        postal_code_elements = shipping_info[constants.UserInfo.POSTAL_CODE]
        for element in postal_code_elements:
            if not element.is_enabled() or not element.is_displayed():
                continue
            if element.get_attribute(constants.ETC.VALUE):
                element.clear()
            # time.sleep(Timer.ONE_SECOND_TIMEOUT)
            element.send_keys(UserInfo.POSTAL_CODE)

        ShipUtils.fill_state_attribute(shipping_info)
        ShipUtils.fill_country_field(shipping_info)

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

        for element in state_element:
            if not element.is_enabled() or not element.is_displayed():
                continue
            if element.tag_name == constants.Tags.INPUT:
                logger.info("Filling state using input")
                # time.sleep(Timer.ONE_SECOND_TIMEOUT)
                element.send_keys(UserInfo.STATE_INPUT)
            else:
                logger.info("Filling state using select option")
                all_options = element.find_elements_by_tag_name(constants.ETC.OPTION)
                for option in all_options:
                    if option.get_attribute(constants.ETC.VALUE) in UserInfo.STATE_OPTIONS:
                        option.click()
                        break
