from modules.utilities import Utils
from modules.constants import Pattern, Tags

class AddToCart():
    def __init__(self, context):
        self.context = context
        self.web = context.web
    
    def find_add_to_(self):
        add_to_dict = self.extract_required_elements()
        required_tag = Utils.get_required_tag(add_to_dict.keys(), Tags.POSSIBLE_ADD_TO_TAGS_LIST)
    
    def extract_required_elements(self):
        try:
            add_to_elements = self.web.finds_by_xpath_wait(Pattern.ADD_TO_PATTERN)
            return Utils.create_dict(add_to_elements)
        except:
            return {}