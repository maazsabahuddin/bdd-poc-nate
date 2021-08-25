# Local imports
import time

# Framework imports
from features.steps import logger
from selenium.common import exceptions
from modules.constants import Tags, Pattern
from modules.utilities import Utils


class BuyNow(object):

    def __init__(self, context):
        self.context = context
        self.web = context.web

    def check_buy_now_page(self):
        self.web.open(self.context.url)

        logger.info("Fetching required elements")

        buy_now_dict = self.fetch_required_elements()
        required_tag = Utils.get_required_tag(buy_now_dict.keys(), Tags.POSSIBLE_BUY_TAGS_LIST)
        element = self.get_element_by_tag(buy_now_dict, required_tag)

        time.sleep(self.web.timeout)

        if element is not None:
            try:
                element.click()
            except (exceptions.StaleElementReferenceException, exceptions.ElementClickInterceptedException):
                print("-----> finding overlay")
                is_cookies_overlay = Utils.accept_cookies(self.web.find_by_xpath_wait)
                time.sleep(self.web.timeout)
                if is_cookies_overlay:
                    buy_now_dict = self.fetch_required_elements()
                    required_tag = Utils.get_required_tag(buy_now_dict.keys(), Tags.POSSIBLE_BUY_TAGS_LIST)
                    element = self.get_element_by_tag(buy_now_dict, required_tag)
                    element.click()
                else:
                    print("------> finding cross button")
                    # cross_element = self.web.find_cross_by_css_selector("button[aria-labelby='Close']")
                    cross_element = self.web.find_cross_by_css_selector_wait("button[class='emailReengagement_close_button']")
                    # cross_element = self.web.find_cross_by_xpath("//*[@title='Close']")
                    print(cross_element.get_attribute("outerHTML"))
                    cross_element.click()
                    time.sleep(self.web.timeout)
                    element.click()
        else:
            cross_element = self.web.find_by_xpath("//button[@aria-label='Close']")
            cross_element.click()

        time.sleep(self.web.timeout)

    def fetch_required_elements(self):
        """
        This function find the all element who has buy text and make a list of it.
        """
        buy_web_elements = self.web.finds_by_xpath_wait(Pattern.BUY_PATTERN)
        buy_now_dict = {}
        for ele in buy_web_elements:

            tag_name = ele.tag_name
            if tag_name in Tags.POSSIBLE_BUY_TAGS_LIST:
                if buy_now_dict.get(tag_name):
                    buy_now_dict.get(tag_name).append(ele)
                else:
                    buy_now_dict.update({
                        tag_name: [ele]
                    })

        return buy_now_dict

    def get_element_by_tag(self, buy_now_dict, tag):
        """
        This function return element from the list on the basis of provided tag.
        :param buy_now_dict:
        :param tag:
        :return:
        """
        if tag is None:
            print("Cannot find the required tag to complete the flow please contact to provider.")
            return tag
        elif tag == "button" or tag == "input":
            return buy_now_dict[tag][0]
        elif tag == "span":
            element = buy_now_dict[tag]  
            element_id = element[0].get_attribute("id")
            search_path = f"//*[@aria-labelledby='{element_id}']"
            return self.web.find_by_xpath_wait(search_path)
        else:
            size_of_tag_list = len(buy_now_dict[tag])
            return buy_now_dict[tag][(size_of_tag_list - 1)]
