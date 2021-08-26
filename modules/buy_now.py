# Local imports
import time

# Framework imports
from selenium.common import exceptions
from modules.constants import Tags, Pattern, SkipScenario
from modules.utilities import Utils


class BuyNow(object):

    def __init__(self, context):
        self.context = context
        self.web = context.web

    def check_buy_now_page(self):
        self.web.open(self.context.url)

        buy_now_dict = self.fetch_required_elements()
        requiredTag = Utils.get_required_tag(buy_now_dict.keys(), Tags.POSSIBLE_BUY_TAGS_LIST)
        element = self.get_element_by_tag(buy_now_dict, requiredTag)

        time.sleep(self.web.timeout)

        if element is not None:
            try:
                element.click()
                self.web.skip_scenario(SkipScenario.SKIP_ADD_TO_CART)
                self.web.context.buy_now_found = True
            except (exceptions.StaleElementReferenceException, exceptions.ElementClickInterceptedException, exceptions.ElementNotInteractableException):
                is_cookies_overlay = Utils.accept_cookies(self.web.find_by_xpath_wait)
                time.sleep(self.web.timeout)
                if is_cookies_overlay:
                    buy_now_dict = self.fetch_required_elements()
                    requiredTag = Utils.get_required_tag(buy_now_dict.keys(), Tags.POSSIBLE_BUY_TAGS_LIST)
                    element = self.get_element_by_tag(buy_now_dict, requiredTag)
                    element.click()
                    self.web.context.buy_now_found = True
                else:
                    # cross_element = self.web.find_cross_by_css_selector("button[aria-labelby='Close']")
                    # cross_element = self.web.find_cross_by_xpath("//*[@title='Close']")
                    try:
                        cross_element = self.web.find_cross_by_css_selector_wait("button[class='emailReengagement_close_button']")
                        cross_element.click()
                    except:
                        self.web.context.buy_now_found = False
                        return
                    time.sleep(self.web.timeout)
                    element.click()
                    self.web.skip_scenario(SkipScenario.SKIP_ADD_TO_CART)
                    self.web.context.buy_now_found = True
        else:
            self.web.context.buy_now_found = False

    def fetch_required_elements(self):
        try:
            buy_web_elements = self.web.finds_by_xpath_wait(Pattern.BUY_PATTERN)
            return Utils.create_dict(buy_web_elements)
        except:
            return {}

    def get_element_by_tag(self, buy_now_dict, tag):
        """
        This function return element from the list on the basis of provided tag.
        :param buy_now_dict:
        :param tag:
        :return:
        """
        if tag is None:
            print("Cannot find the required tag to complete the flow please contact to provider.")
            return None
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
