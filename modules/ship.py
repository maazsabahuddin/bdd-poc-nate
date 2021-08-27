# Python Imports
import time

# Local Imports
from modules import constants
from modules.constants import Pattern
from modules.logger import logger
from modules.utilities import Utils


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

        continue_elements = self.web.finds_by_xpath_wait(Pattern.CONTINUE)
        for ele in continue_elements:
            print(ele.tag_name)

        continue_click_element = \
            Utils.fetch_required_elements(continue_elements, constants.Tags.POSSIBLE_CONTINUE_BUTTON)

        if continue_click_element:
            print("FOUND")
            print(continue_click_element)
            extracted_element_tag = Utils.get_required_tag(continue_click_element.keys(),
                                                           constants.Tags.POSSIBLE_CONTINUE_BUTTON)
            # print(continue_click_element[extracted_element_tag][0].get_attribute('outerHTML'))
            # print(continue_click_element[extracted_element_tag][0].is_enabled())
            # print(continue_click_element[extracted_element_tag][0].is_displayed())
            # print(continue_click_element[extracted_element_tag][0].tag_name)
            print(continue_click_element['span'][0].tag_name)
            print(continue_click_element['button'][0].tag_name)
            # continue_click_element['span'][0].click()

        # print(continue_element.tag_name)
        # print("Length of continue element is =>", len(continue_element))
        # if continue_element.tag_name == constants.Tags.BUTTON:
        #     continue_element.click()
        # else:
        #     parent_element = \
        #         Utils.find_parent_element_from_child(continue_element, constants.Tags.POSSIBLE_CONTINUE_BUTTON)
        #     if parent_element:
        #         print("FOUND")
        #         parent_element.click()

        print("DONE CLICKING")
        time.sleep(15)

        return

    @staticmethod
    def identify_shipping_page_type():
        logger.info("Identifying shipping address page type")
        pass

    @staticmethod
    def fill_address_details():
        logger.info("Entering shipping address details.")
        pass
