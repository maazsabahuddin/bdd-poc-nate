# Python imports

# Local imports
from modules.logger import logger
from utility.constants import Pattern, TagsList


class CookiesPopUp:
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.__accept_cookies_element = None

    def find_accept_cookies(self, is_element_belong_to_required_element):
        self.__accept_cookies_element = self.__extract_required_element(Pattern.ACCEPT_COOKIES_PATTERN,
                                                                        is_element_belong_to_required_element)

    def __extract_required_element(self, pattern, is_element_belong_to_required_element):
        cookies_elements = self.web.find_by_xpath(pattern)
        return is_element_belong_to_required_element(cookies_elements, TagsList.POSSIBLE_COOKIES_ELEMENTS)

    def accept_cookies(self):
        try:
            if not self.__accept_cookies_element:
                return False
            self.__accept_cookies_element.click()
            return True
        except Exception as e:
            logger.info("cookies pop up exception: ", str(e))
            return False
