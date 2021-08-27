# Python Imports
import time

# Local Imports
from modules.constants import Pattern
from modules.logger import logger


class Shipping:
    """
    This class is responsible to fill out shipping address details by identify
    shipping page type and other flows.
    """
    def __init__(self, context):
        self.context = context
        self.web = context.web

    # def get_element_by_tag(self, buy_now_dict, tag):
    #     """
    #     This function return element from the list on the basis of provided tag.
    #     :param buy_now_dict:
    #     :param tag:
    #     :return:
    #     """
    #     if tag is None:
    #         logger.info("Cannot find the required tag to complete the flow please contact to provider.")
    #         return tag
    #     elif tag == Tags.BUTTON or tag == Tags.INPUT:
    #         return buy_now_dict[tag][0]
    #     elif tag == Tags.SPAN:
    #         element = buy_now_dict[tag]
    #         element_id = element[0].get_attribute("id")
    #         search_path = f"//*[@aria-labelledby='{element_id}']"
    #         return self.web.find_by_xpath_wait(search_path)
    #     else:
    #         size_of_tag_list = len(buy_now_dict[tag])
    #         return buy_now_dict[tag][(size_of_tag_list - 1)]

    def get_required_elements(self):
        self.web.open(self.context.url)
        logger.info("get required elements")
        time.sleep(20)

        first_name_element = self.web.find_by_xpath(Pattern.FIRST_NAME)
        last_name_element = self.web.find_by_xpath(Pattern.LAST_NAME)
        email_element = self.web.find_by_xpath(Pattern.EMAIL)
        phone_element = self.web.find_by_xpath(Pattern.PHONE)
        address1_element = self.web.find_by_xpath(Pattern.ADDRESS1)
        address2_element = self.web.find_by_xpath(Pattern.ADDRESS2)
        city_element = self.web.find_by_xpath(Pattern.CITY)
        state_element = self.web.find_by_xpath(Pattern.STATE)
        postal_code_element = self.web.find_by_xpath(Pattern.POSTAL_CODE)

        first_name_element.send_keys("some Maaz")
        last_name_element.send_keys("some MaazMaazMaazMaaz")
        email_element.send_keys("maaz@gmail.com")
        phone_element.send_keys("17238912739")
        address1_element.send_keys("Home A1, 0th street, Houston.")
        address2_element.send_keys("Opposite to Alwa Bridge")
        city_element.send_keys("City")
        postal_code_element.send_keys("41015")

        all_options = state_element.find_elements_by_tag_name("option")
        for option in all_options:
            if "LA" in option.get_attribute("value"):
                option.click()

        continue_element = self.web.find_by_xpath(Pattern.CONTINUE)
        try:
            continue_element.click()
        except Exception as e:
            logger.info(str(e))
            print(continue_element)
            print("Caught exception")
            print(dir(continue_element.parent))
            # continue_element.parent.click()

        time.sleep(5)

        return

    @staticmethod
    def identify_shipping_page_type():
        logger.info("Identifying shipping address page type")
        pass

    @staticmethod
    def fill_address_details():
        logger.info("Entering shipping address details.")
        pass
