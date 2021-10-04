# Local imports
from utility.utilities import Utils
from utility.constants import Pattern, SkipScenario, TagsList

class KeyWords:

    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.is_keywords_found = False

    def find_keywords(self):
        self.extract_required_elements(Pattern.KeyWords)

    def skip_checkout_step_2(self):
        self.web.skip_scenario(SkipScenario.SKIP_CHECKOUT_STEP_2)

    def extract_required_elements(self, pattern):
        keywords_elements = self.web.finds_by_xpath_wait(pattern)
        return Utils.fetch_required_elements(keywords_elements, TagsList.POSSIBLE_ADD_TO_TAGS_LIST)