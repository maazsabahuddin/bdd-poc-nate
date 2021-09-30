# Local imports
import time
from modules.logger import logger
from utility.constants import Pattern, Timer


class PromotionPopUp:
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.__promotion_elements = None
        self.is_promo_overlay_closed = False
        self.__promotion_iframes = None

    def find_promotion_elements(self):
        self.__promotion_elements = self.__extract_required_elements(Pattern.PROMOTION_OVERLAY_PATTERN)
        if not self.__promotion_elements:
            self.__promotion_iframes = self.__find_iframe_element()
        
    def __extract_required_elements(self, pattern):
        active_promotion_elements = []
        promotion_elements = self.web.find_by_xpath(pattern)
        if not promotion_elements:
            return active_promotion_elements

        for promotion_element in promotion_elements:
            if promotion_element.is_enabled() and promotion_element.is_displayed():
                active_promotion_elements.append(promotion_element)

        return active_promotion_elements

    def close_promotion_dialog(self):
        if not self.__promotion_elements:
            if self.__promotion_iframes:
                self.__find_element_and_close_promotion_iframe()
            else:
                return self.is_promo_overlay_closed

        for element in self.__promotion_elements:
            try:
                element.click()
                self.is_promo_overlay_closed = True
            except Exception as e:
                logger.info("In exception of promotion: ", str(e))

        return self.is_promo_overlay_closed

    def __find_iframe_element(self):
        iframe_pattern = "//iframe[@id='ju_iframe_727313' or @id='ju_iframe_439916']"
        return self.web.finds_by_xpath_wait(iframe_pattern)

    def __find_element_and_close_promotion_iframe(self):
        for iframe in self.__promotion_iframes:
            self.web.switch_to_frame(iframe)
            promo_element = self.__extract_required_elements(Pattern.PROMOTION_OVERLAY_PATTERN)
            if not promo_element:
                continue
            for element in promo_element:
                element.click()
                self.is_promo_overlay_closed = True
                time.sleep(Timer.FIVE_SECOND_TIMEOUT)
            self.web.switch_to_default_content()
