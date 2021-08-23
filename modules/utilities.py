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
    
    # This function takes list of elements extracted from the DOM file then separate element according to it's type
    @staticmethod
    def create_dict(list_of_elements):
        elements_dict = {}
        for element in list_of_elements:
            if (element.tag_name == "button"):
                if ("button" not in elements_dict):
                    elements_dict["button"] = [element]
                else:
                    button_list = elements_dict["button"]
                    button_list.append(element)
                    elements_dict["button"] = button_list
            if (element.tag_name == "input"):
                if ("input" not in elements_dict):
                    elements_dict["input"] = [element]
                else:
                    input_list = elements_dict["input"]
                    input_list.append(element)
                    elements_dict["input"] = input_list
            if (element.tag_name == "a"):
                if ("a" not in elements_dict):
                    elements_dict["a"] = [element]
                else:
                    a_list = elements_dict["a"]
                    a_list.append(element)
                    elements_dict["a"] = a_list
            if (element.tag_name == "span"):
                if ("span" not in elements_dict):
                    elements_dict["span"] = [element]
                else:
                    span_list = elements_dict["span"]
                    span_list.append(element)
                    elements_dict["span"] = span_list
        return elements_dict
    
    # This function get element from the given list on the basis of given element key
    @staticmethod
    def get_required_element_by_key(key, elements_list):
        if (key is None):
            print("Cannot find the required tag to complete the flow please contact to provider.")
            return None
        else:
            return elements_list[key][0]