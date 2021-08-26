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
        time.sleep(23)
        # wait = WebDriverWait(browser, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, ".//input[@value='Submit' and @type='submit']"))).click()
        first_name_element = self.web.find_by_xpath(Pattern.FIRST_NAME)
        last_name_element = self.web.find_by_xpath(Pattern.LAST_NAME)
        # email_element = self.web.finds_by_xpath_wait(Pattern.EMAIL)
        # phone_element = self.web.finds_by_xpath_wait(Pattern.PHONE)
        # address1_element = self.web.finds_by_xpath_wait(Pattern.ADDRESS1)
        # address2_element = self.web.finds_by_xpath_wait(Pattern.ADDRESS2)
        # city_element = self.web.finds_by_xpath_wait(Pattern.CITY)
        # state_element = self.web.finds_by_xpath_wait(Pattern.STATE)
        # postal_code_element = self.web.finds_by_xpath_wait(Pattern.POSTAL_CODE)

        # self.web.finds_by_xpath_and_set_attribute(Pattern.FIRST_NAME, value="Maaz")
        print(f"FNE => {first_name_element}")
        first_name_element.send_keys("some Maaz")
        last_name_element.send_keys("some MaazMaazMaazMaaz")
        # first_name_element.click()
        # print(email_element)
        # print(phone_element)
        # print(address1_element)
        # print(address2_element)
        # print(city_element)
        # print(state_element)
        # print(postal_code_element)

        return

    @staticmethod
    def identify_shipping_page_type():
        logger.info("Identifying shipping address page type")
        pass

    @staticmethod
    def fill_address_details():
        logger.info("Entering shipping address details.")
        pass
