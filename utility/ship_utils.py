# Framework imports
from selenium.common.exceptions import StaleElementReferenceException

# Local imports
from modules.logger import logger
from utility import constants


class ShipUtils:

    @staticmethod
    def fill_name_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling name fields")
        if len(shipping_info[constants.UserInfo.FULL_NAME]) > 0:
            try:
                shipping_info[constants.UserInfo.FULL_NAME][0].send_keys("Maaz Sabah Uddin")
            except StaleElementReferenceException as e:
                pass

        print(shipping_info[constants.UserInfo.FIRST_NAME])
        if len(shipping_info[constants.UserInfo.FIRST_NAME]) > 0:
            try:
                shipping_info[constants.UserInfo.FIRST_NAME][0].send_keys("Maaz")
            except StaleElementReferenceException as e:
                pass

        if len(shipping_info[constants.UserInfo.LAST_NAME]) > 0:
            try:
                shipping_info[constants.UserInfo.LAST_NAME][0].send_keys("Sabah Uddin")
            except StaleElementReferenceException as e:
                pass

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
                    element.send_keys("maaz@gmail.com")
            except StaleElementReferenceException as e:
                shipping_info[constants.UserInfo.EMAIL][0].send_keys("maaz@gmail.com")
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
            shipping_info[constants.UserInfo.COUNTRY_CODE][0].send_keys("92")
            shipping_info[constants.UserInfo.PHONE][0].send_keys("6473479480")

        if shipping_info[constants.UserInfo.PHONE] and not shipping_info[constants.UserInfo.COUNTRY_CODE]:
            shipping_info[constants.UserInfo.PHONE][0].send_keys("+12473479480")

    @staticmethod
    def fill_address_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling address related fields")
        if shipping_info[constants.UserInfo.ADDRESS1]:
            shipping_info[constants.UserInfo.ADDRESS1][0].send_keys("Home A1, 0th street, Houston.")

        if shipping_info[constants.UserInfo.ADDRESS2]:
            shipping_info[constants.UserInfo.ADDRESS2][0].send_keys("Opposite to Alwa Bridge")

        if shipping_info[constants.UserInfo.CITY]:
            shipping_info[constants.UserInfo.CITY][0].send_keys("City")

        if shipping_info[constants.UserInfo.POSTAL_CODE]:
            shipping_info[constants.UserInfo.POSTAL_CODE][0].send_keys("10710")

        ShipUtils.fill_state_attribute(shipping_info)

    @staticmethod
    def fill_state_attribute(shipping_info):
        """
        Filling state element with respect to its tag that can be [INPUT, SELECT]
        :param shipping_info:
        :return:
        """
        state_element = shipping_info[constants.UserInfo.STATE][0]
        if state_element.tag_name == constants.Tags.INPUT:
            logger.info("Filling state using input")
            state_element.send_keys("Ontario")
        else:
            logger.info("Filling state using select option")
            all_options = state_element.find_elements_by_tag_name("option")
            for option in all_options:
                if option.get_attribute("value") in ["MA", "USLA", "LA", "AL", "California"]:
                    option.click()
