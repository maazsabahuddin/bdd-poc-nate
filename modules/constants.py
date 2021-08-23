class Tags:
    POSSIBLE_BUY_TAGS_LIST = ["button", "input", "a", "span"]


class Pattern:
    BUY_PATTERN = "//*[contains(text(),'Buy') or contains(text(),'BUY')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(text(),'Accept') and contains(text(),'Cookies')) or (contains(text(),'Accept') and contains(text(),'cookies')) or (contains(text(),'accept') and contains(text(),'cookies'))]"


class Scenarios:
    LOGIN = "login"
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
