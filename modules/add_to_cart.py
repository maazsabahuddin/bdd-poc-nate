import time
from modules.utilities import Utils
from modules.constants import Pattern, Tags

class AddToCart():
    required_element = None
    def __init__(self, context):
        self.context = context
        self.web = context.web
    
    def find_add_to_(self):
        add_to_dict = self.extract_required_elements()
        required_tag = Utils.get_required_tag(add_to_dict.keys(), Tags.POSSIBLE_ADD_TO_TAGS_LIST)
        self.required_element = Utils.get_required_element_by_key(required_tag, add_to_dict)

    def extract_required_elements(self):
        try:
            add_to_elements = self.web.finds_by_xpath_wait(Pattern.ADD_TO_PATTERN)
            return Utils.create_dict(add_to_elements)
        except:
            return {}
    
    def hit_add_to_cart_element(self):
        try:
            self.required_element.click()
            time.sleep(self.web.timeout)
        except:
            print("exception found")
