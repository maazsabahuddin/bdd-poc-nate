import time
# Framework imports
from selenium.common import exceptions
# Local imports
from utility.constants import Tags, Pattern, SkipScenario, Timer
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
        required_element = Utils.get_required_element(requiredTag, buy_now_dict)
        if (required_element is not None):
            self.is_buy_now_found = True
        self.required_element = required_element

    def fetch_required_elements(self):
        buy_web_elements = self.web.finds_by_xpath_wait(Pattern.BUY_PATTERN)
        return Utils.fetch_required_elements(buy_web_elements, Tags.POSSIBLE_BUY_TAGS_LIST)

    def skip_non_required_scenarios(self):
        """
        This function set the skip scenarios tags which are not required after running buy now button successfully.
        """
        self.web.skip_scenario(SkipScenario.SKIP_ADD_TO_CART)
        self.web.skip_scenario(SkipScenario.SKIP_PROCEED_CHECKOUT)

    def hit_buy_now_element(self):
        """
        This function click on the provided element
        """
        try:
            self.required_element.click()
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
        except (exceptions.StaleElementReferenceException, exceptions.ElementClickInterceptedException, exceptions.ElementNotInteractableException) as e:
            is_cookies_overlay = Utils.accept_cookies(self.web.find_by_xpath_wait)
            time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
            if is_cookies_overlay:
                self.check_buy_now_page()
                self.required_element.click()
            else:
                # cross_element = self.web.find_cross_by_css_selector("button[aria-labelby='Close']")
                # cross_element = self.web.find_cross_by_xpath("//*[@title='Close']")
                try:
                    cross_element = self.web.find_cross_by_css_selector_wait("button[class='emailReengagement_close_button']")
                    cross_element.click()
                except:
                    return
                time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
                self.required_element.click()            
        