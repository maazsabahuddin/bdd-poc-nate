from modules.constants import Tags, Pattern
from selenium.common import exceptions

class Utils:
    """ 
    This function get element from the provided list on priority basis.
    Priority is: 1-button, 2-input, 3-a, 4-span
    """
    @staticmethod
    def get_required_tag(tags, priorityTagsList):
        for tag in priorityTagsList:
            if tag in tags:
                return tag
        return None
    
    # This function accept cookies overlay before clicking on buy button
    @staticmethod
    def accept_cookies(find_by_xpath):
        try:
            overlay_elements = find_by_xpath(Pattern.ACCEPT_COOKIES_PATTERN)
            if (overlay_elements is not None):
                overlay_elements.click()
                return True
            else:
                return False
        except exceptions.TimeoutException:
            return False