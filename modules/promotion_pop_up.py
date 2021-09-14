# Python imports
import time

# Local imports
from modules.logger import logger
from utility.constants import Pattern, Timer


class PromotionPopUp:
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.__promotion_elements = None

    def find_promotion_elements(self):
        self.__promotion_elements = self.__extract_required_elements(Pattern.PROMOTION_OVERLAY_PATTERN)
        print(self.__promotion_elements)

    def __extract_required_elements(self, pattern):
        active_promotion_elements = []
        promotion_elements = self.web.finds_by_xpath(pattern)
        if promotion_elements is not None:
            for promotion_element in promotion_elements:
                if promotion_element.is_enabled() and promotion_element.is_displayed():
                    active_promotion_elements.append(promotion_element)
            return active_promotion_elements
        return None

    def close_promotion_dialog(self):
        if self.__promotion_elements is not None:
            for element in self.__promotion_elements:
                try:
                    element.click()
                    time.sleep(Timer.PROCESS_PAUSE_TIMEOUT)
                except Exception as e:
                    logger.info(f"Exception on element: {element.get_attribute('outerHTML')} of {str(e)}")
