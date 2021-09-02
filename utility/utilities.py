# Framework Imports
from selenium.common import exceptions

# Local imports
from utility import constants


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
            overlay_elements = find_by_xpath(constants.Pattern.ACCEPT_COOKIES_PATTERN)
            if overlay_elements is not None:
                overlay_elements.click()
                return True
            else:
                return False
        except exceptions.TimeoutException:
            pass

    @staticmethod
    def get_required_element(tag, elements_list):
        """
        This function returns element from the elements dict
        """
        if tag is None:
            return None
        else:
            for element in elements_list[tag]:
                if element.is_enabled() and element.is_displayed():
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
                # print(parent_element)
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
            for _ in range(8):
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
            if 'guest' in element.get_attribute(attribute_name):
                if element.is_enabled() and element.is_displayed():
                    return element
        return None
