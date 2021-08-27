from modules.constants import Tags, Pattern
from selenium.common import exceptions

class Utils:

    @staticmethod
    def get_required_tag(tags, priorityTagsList):
        """
        This function return element tag from the provided list on priority basis.
        """
        for tag in priorityTagsList:
            if tag in tags:
                return tag
        return None
    
    @staticmethod
    def accept_cookies(find_by_xpath):
        """
        This function accept cookies overlay before clicking on buy button
        """
        overlay_elements = find_by_xpath(Pattern.ACCEPT_COOKIES_PATTERN)
        if (overlay_elements is not None):
            overlay_elements.click()
            return True
        else:
            return False
 
    @staticmethod
    def get_required_element_by_key(key, elements_list, area):
        """
        This function returns element from the elements dict
        """
        if (key is None):
            print("Cannot find the required tag in ", area)
            return None
        else:
            return elements_list[key][0]
    
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
            for _ in range(2):
                parent_element = current_found_element.find_element_by_xpath("..")
                if (parent_element.tag_name in filter_list):
                    return parent_element
                else:
                    current_found_element = parent_element
            return None
        except exceptions.NoSuchElementException:
            return None
