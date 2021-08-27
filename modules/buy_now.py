import time
# Framework imports
from selenium.common import exceptions
# Local imports
from utility.constants import Tags, Pattern, SkipScenario
from utility.utilities import Utils


class BuyNow(object):

    def __init__(self, context):
        self.context = context
        self.web = context.web
        self.is_buy_now_found = False

    def check_buy_now_page(self):
        self.web.open(self.context.url)

        buy_now_dict = self.fetch_required_elements()
        requiredTag = Utils.get_required_tag(buy_now_dict.keys(), Tags.POSSIBLE_BUY_TAGS_LIST)
        element = self.get_element_by_tag(buy_now_dict, requiredTag)

        if element is not None:
            try:
                element.click()
                self.is_buy_now_found = True
            except (exceptions.StaleElementReferenceException, exceptions.ElementClickInterceptedException, exceptions.ElementNotInteractableException) as e:
                is_cookies_overlay = Utils.accept_cookies(self.web.find_by_xpath_wait)
                time.sleep(self.web.timeout)
                if is_cookies_overlay:
                    buy_now_dict = self.fetch_required_elements()
                    requiredTag = Utils.get_required_tag(buy_now_dict.keys(), Tags.POSSIBLE_BUY_TAGS_LIST)
                    element = self.get_element_by_tag(buy_now_dict, requiredTag)
                    element.click()
                    self.is_buy_now_found = True
                else:
                    # cross_element = self.web.find_cross_by_css_selector("button[aria-labelby='Close']")
                    # cross_element = self.web.find_cross_by_xpath("//*[@title='Close']")
                    try:
                        cross_element = self.web.find_cross_by_css_selector_wait("button[class='emailReengagement_close_button']")
                        cross_element.click()
                    except:
                        return
                    time.sleep(self.web.timeout)
                    element.click()
                    self.is_buy_now_found = True

    def fetch_required_elements(self):
        buy_web_elements = self.web.finds_by_xpath_wait(Pattern.BUY_PATTERN)
        return Utils.fetch_required_elements(buy_web_elements, Tags.POSSIBLE_BUY_TAGS_LIST)

    def get_element_by_tag(self, buy_now_dict, tag):
        """
        This function return element from the list on the basis of provided tag.
        :param buy_now_dict:
        :param tag:
        :return:
        """
        if tag is None:
            return None
        else:
            for element in buy_now_dict[tag]:
                if (element.is_enabled() and element.is_displayed()):
                    return element
            return None

    def skip_non_required_scenarios(self):
        """
        This function set the skip scenarios tags which are not required after running buy now button successfully.
        """
        self.web.skip_scenario(SkipScenario.SKIP_ADD_TO_CART)
        self.web.skip_scenario(SkipScenario.SKIP_PROCEED_CHECKOUT)
        