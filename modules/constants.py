class Tags:
    POSSIBLE_BUY_TAGS_LIST = ["button", "input", "a", "span"]
    POSSIBLE_ADD_TO_TAGS_LIST = ["button", "span", "input"]

class Pattern:
    BUY_PATTERN = "//*[contains(text(),'Buy') or contains(text(),'BUY')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(text(),'Accept') and contains(text(),'Cookies')) or (contains(text(),'Accept') and contains(text(),'cookies')) or (contains(text(),'accept') and contains(text(),'cookies'))]"
    ADD_TO_PATTERN = "//*[contains(text(), 'ADD TO BAG') or contains(text(), 'Add to BAG') or contains(text(), 'Add To BAG') or contains(text(), 'Add to Cart') or contains(text(), 'ADD TO CART') or contains(text(), 'Add to cart') or contains(@value, 'Add to Cart')]"

class Scenario:
    LOGIN = "login"
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"