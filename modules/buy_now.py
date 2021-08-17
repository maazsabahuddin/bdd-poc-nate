import time
import logging
from modules.constants import Tags, Pattern
from selenium.common import exceptions

class BuyNow(object):

    def __init__(self, context):
        self.context = context
        self.web = context.web

    def check_buy_now_page(self):
        self.web.open(self.context.url)
        try:
            buy_now_dict = self.fetch_required_elements()
        except exceptions.StaleElementReferenceException:
            is_overlay_removed = self.fetch_overlay_details()
            if (is_overlay_removed):
                buy_now_dict = self.fetch_required_elements()
            else:
                buy_now_dict = {}

        requiredTag = self.get_required_tag(buy_now_dict.keys())
        element = self.get_element_by_tag(buy_now_dict, requiredTag)

        if (element is not None):
            try:
                element.click()
            except exceptions.ElementClickInterceptedException:
                cross_element = self.web.find_cross_by_css_selector('button[aria-label="Close panel"]')
                cross_element.click()
                time.sleep(self.web.timeout)
                element.click()
        else:
            cross_element = self.web.find_cross_by_css_selector('button[aria-label="Close panel"]')
            cross_element.click()


        time.sleep(3)

    """
    This function find the all element who has buy text and make a list of it.
    """
    def fetch_required_elements(self):
        buy_web_elements = self.web.finds_by_xpath(Pattern.BUY_PATTERN)
        buy_now_dict = {}
        for ele in buy_web_elements:
            if (ele.tag_name == "button"):
                if ("button" not in buy_now_dict):
                    buy_now_dict["button"] = [ele]
                else:
                    button_list = buy_now_dict["button"]
                    button_list.append(ele)
                    buy_now_dict["button"] = button_list
            if (ele.tag_name == "input"):
                if ("input" not in buy_now_dict):
                    buy_now_dict["input"] = [ele]
                else:
                    input_list = buy_now_dict["input"]
                    input_list.append(ele)
                    buy_now_dict["input"] = input_list
            if (ele.tag_name == "a"):
                if ("a" not in buy_now_dict):
                    buy_now_dict["a"] = [ele]
                else:
                    a_list = buy_now_dict["a"]
                    a_list.append(ele)
                    buy_now_dict["a"] = a_list
            if (ele.tag_name == "span"):
                if ("span" not in buy_now_dict):
                    buy_now_dict["span"] = [ele]
                else:
                    span_list = buy_now_dict["span"]
                    span_list.append(ele)
                    buy_now_dict["span"] = span_list
        return buy_now_dict

    """ 
    This function get element from the list on the priority basis.
    Priority is:
    1- button
    2- input
    3- a
    4- span
    """
    def get_required_tag(self, tags):
        for tag in Tags.POSSIBLE_BUY_TAGS_LIST:
            if tag in tags:
                return tag
        return None

    """
    This function return element from the list on the basis of provided tag.
    """
    def get_element_by_tag(self, buy_now_dict, tag):
        if (tag is None):
            print("Cannot find the required tag to complete the flow please contact to provider.")
            return None
        elif (tag == "button" or tag == "input"):
            return buy_now_dict[tag][0]
        elif (tag == "span"):
            element = buy_now_dict[tag]  
            element_id = element[0].get_attribute("id")
            search_path = f"//*[@aria-labelledby='{element_id}']"
            return self.web.find_by_xpath(search_path)
        else:
            size_of_tag_list = len(buy_now_dict[tag])
            return buy_now_dict[tag][(size_of_tag_list - 1)]

    """
    This function accept cookies overlay before clicking on buy button
    """
    def fetch_overlay_details(self):
        overlay_elements = self.web.find_elements_by_xpath(Pattern.ACCEPT_COOKIES_PATTERN)
        accept_element = None
        for ele in overlay_elements:
            accept_element = ele
            break
        if (accept_element is not None):
            accept_element.click()
            return True
        else:
            return False