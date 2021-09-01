from modules.logger import logger
from utility import constants
from utility.utilities import Utils


class ShipUtils:

    @staticmethod
    def fill_name_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling name fields")
        full_name = shipping_info[constants.ETC.FULL_NAME]
        if full_name:
            shipping_info[constants.ETC.FULL_NAME][0].send_keys("Maaz Sabah Uddin")
        else:
            shipping_info[constants.ETC.FIRST_NAME][0].send_keys("Maaz")
            shipping_info[constants.ETC.LAST_NAME][0].send_keys("Sabah Uddin")

    @staticmethod
    def fill_email_field(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling email field")
        print(shipping_info[constants.ETC.EMAIL])
        for element in shipping_info[constants.ETC.EMAIL]:
            if element.is_enabled() and element.is_displayed():
                element.send_keys("maaz@gmail.com")

    @staticmethod
    def fill_phone_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling phone related fields")
        if shipping_info[constants.ETC.COUNTRY_CODE]:
            shipping_info[constants.ETC.COUNTRY_CODE][0].send_keys("92")
            shipping_info[constants.ETC.PHONE][0].send_keys("6473479480")

        if shipping_info[constants.ETC.PHONE] and not shipping_info[constants.ETC.COUNTRY_CODE]:
            shipping_info[constants.ETC.PHONE][0].send_keys("+12473479480")

    @staticmethod
    def fill_address_related_fields(shipping_info):
        """
        This function is responsible to fill out all the related fields with address
        :param shipping_info:
        :return:
        """
        logger.info("Filling address related fields")
        shipping_info[constants.ETC.ADDRESS1][0].send_keys("Home A1, 0th street, Houston.")
        if shipping_info[constants.ETC.ADDRESS2]:
            shipping_info[constants.ETC.ADDRESS2][0].send_keys("Opposite to Alwa Bridge")

        shipping_info[constants.ETC.CITY][0].send_keys("City")
        shipping_info[constants.ETC.POSTAL_CODE][0].send_keys("10710")

        ShipUtils.fill_state_attribute(shipping_info)

    @staticmethod
    def fill_state_attribute(shipping_info):
        """
        Filling state element with respect to its tag that can be [INPUT, SELECT]
        :param shipping_info:
        :return:
        """
        state_element = shipping_info[constants.ETC.STATE][0]
        if state_element.tag_name == constants.Tags.INPUT:
            logger.info("Filling state using input")
            state_element.send_keys("Ontario")
        else:
            logger.info("Filling state using select option")
            all_options = state_element.find_elements_by_tag_name("option")
            for option in all_options:
                if option.get_attribute("value") in ["MA", "USLA", "LA", "AL", "California"]:
                    option.click()
