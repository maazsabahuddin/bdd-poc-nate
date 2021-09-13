# Python imports
import time

# Local imports
from utility.utilities import Utils
from utility.constants import Pattern, TagsList, Timer


class CookiesPopUp:
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.__accept_cookies_element = None

    def find_accept_cookies(self):
        cookies_element = self.__extract_required_element(Pattern.ACCEPT_COOKIES_PATTERN)
        if cookies_element is None:
            return
        self.__accept_cookies_element = cookies_element
        time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)

    def __extract_required_element(self, pattern):
        cookies_element = self.web.find_by_xpath(pattern)
        return Utils.is_element_belong_to_required_element(cookies_element, TagsList.POSSIBLE_COOKIES_ELEMENTS)

    def accept_cookies(self):
        try:
            if self.__accept_cookies_element is not None:
                self.__accept_cookies_element.click()
                time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
                return True
            else:
                return False
        except Exception as e:
            print("cookies pop up  exception: ", str(e))
            return False
