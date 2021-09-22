# Python imports
import multiprocessing

# Framework imports
from modules.promotion_pop_up import PromotionPopUp
from selenium.common import exceptions

# Local imports
from utility.constants import Pattern, Tags
from modules.cookies_pop_up import CookiesPopUp


class Utils:

    @staticmethod
    def get_required_tag(tags, priority_tags_list):
        """
        This function return element tag from the provided list on priority basis.
        """
        for tag in priority_tags_list:
            if tag in tags:
                return tag
        return None
    
    @staticmethod
    def accept_cookies(find_by_xpath):
        """
        This function accept cookies overlay before clicking on buy button
        """
        try:
            overlay_elements = find_by_xpath(Pattern.ACCEPT_COOKIES_PATTERN)
            if overlay_elements is not None:
                overlay_elements.click()
                return True
            return False
        except exceptions.TimeoutException:
            return True

    @staticmethod
    def get_required_element(tag, elements_dict):
        """
        This function returns element from the elements dict
        """
        for element in elements_dict[tag]:
            if element.is_enabled() and element.is_displayed():
                return element
            elif element.is_enabled() and element.get_attribute("type") == "radio" and element.tag_name == Tags.INPUT:
                return element
        return None

    @staticmethod
    def fetch_required_elements(elements, filter_list):
        """
        This function returns filter dict from extracted elements
        """
        result_dict = {}
        # if no elements found, return empty dict
        if len(elements) == 0:
            return result_dict

        for ele in elements:
            tag_name = ele.tag_name
            # handling case of span - here we find the parent element of span and check in list
            if tag_name == "span":
                # find its parent element and check its tag
                parent_element = Utils.find_parent_element_from_child(ele, filter_list)
                if parent_element is not None:
                    tag_name = parent_element.tag_name
                    ele = parent_element
            if tag_name in filter_list:
                if result_dict.get(tag_name):
                    result_dict.get(tag_name).append(ele)
                else:
                    result_dict.update({
                        tag_name: [ele]
                    })
        return result_dict

    @staticmethod
    def find_parent_element_from_child(child_element, filter_list):
        """
        This function returns parent element up to 2 level from child element
        """
        try:
            current_found_element = child_element
            for _ in range(5):
                parent_element = current_found_element.find_element_by_xpath("..")
                if parent_element.tag_name in filter_list:
                    return parent_element
                current_found_element = parent_element
            return None
        except exceptions.NoSuchElementException:
            return None

    @staticmethod
    def get_required_element_related_to_guest(tag, elements_dict):
        """
        This function take a tag name and dictionary of found elements,
        it will futher filter the dictionary to find the guest related element
        """
        attribute_name = "class"
        if tag == "input":
            attribute_name = "name"
        for element in elements_dict[tag]:
            attribute = element.get_attribute(attribute_name)
            if attribute == None or attribute == "":
                attribute = element.get_attribute("outerText")
                attribute = attribute.lower()
            if 'guest' in attribute or 'Guest' in attribute:
                if element.is_enabled() and element.is_displayed():
                    return element
        return None

    @staticmethod
    def get_required_element_2(element_dict, tag_priority_list):
        """
        This function take element dictionary and priority list of elements.
        This will loop over the list and find the tag in dictionary if found,
        then fetch element and test if it's enabled and displayed then return either
        search for the next element in list.
        """
        for tag in tag_priority_list:
            if tag in element_dict.keys():
                element = Utils.get_required_element(tag, element_dict)
                if element:
                    return element
        return None

    @staticmethod
    def is_element_belong_to_required_element(elements, list_of_element):
        """
        This function takes list of elements and priority list, to extract
        required element from the given elements list.
        """
        if elements is not None:
            for element in elements:
                tag_name = element.tag_name
                if tag_name in list_of_element:
                    if element.is_enabled() and element.is_displayed():
                        return element
        return None

    @staticmethod
    def check_cookies_overlay(context, overlay_dict):
        cookies_pop_up = CookiesPopUp(context)
        cookies_pop_up.find_accept_cookies(Utils.is_element_belong_to_required_element)
        overlay_dict['cookies'] = cookies_pop_up.accept_cookies()

    @staticmethod
    def check_promotional_overlay(context, overlay_dict):
        promotions = PromotionPopUp(context)
        promotions.find_promotion_elements()
        overlay_dict['promotion'] = promotions.close_promotion_dialog()

    @staticmethod
    def check_overlays(context):
        manager = multiprocessing.Manager()
        overlay_dict = manager.dict()

        process1 = multiprocessing.Process(target=Utils.check_cookies_overlay(context, overlay_dict))
        process2 = multiprocessing.Process(target=Utils.check_promotional_overlay(context, overlay_dict))
        
        process1.start()
        process2.start()
        
        process1.join()
        process2.join()

        if True in overlay_dict.values():
            return True
        else:
            return False

    @staticmethod
    def extract_required_element_2(list_of_elements):
        if list_of_elements:
            for element in list_of_elements:
                if (element.tag_name == Tags.INPUT or element.tag_name == Tags.SELECT) and (element.is_enabled() and element.is_displayed()):
                    return element
        return None

    @staticmethod
    def fetch_required_elements3(elements, filter_list):
        """
        This function returns filter dict from extracted elements
        """
        result_dict = {}
        # if no elements found, return empty dict
        if len(elements) == 0:
            return result_dict

        for ele in elements:
            tag_name = ele.tag_name
            if tag_name in filter_list:
                if result_dict.get(tag_name):
                    result_dict.get(tag_name).append(ele)
                else:
                    result_dict.update({
                        tag_name: [ele]
                    })
        return result_dict
