class Tags:
    POSSIBLE_BUY_TAGS_LIST = ["button", "input", "a", "span"]
    POSSIBLE_ADD_TO_TAGS_LIST = ["button", "span", "input"]


class Pattern:
    BUY_PATTERN = "//*[contains(translate(text(), 'BUY', 'buy'), 'buy')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(translate(text(), 'ACEPT', 'acept'), 'accept') and contains(translate(text(), 'COKIES', 'cokies'), 'cookies') or contains(translate(@name, 'ACEPT', 'acept'), 'accept'))]"
    ADD_TO_PATTERN = "//*[contains(translate(text(), 'ABDGOT', 'abdgot'), 'add to bag') or contains(translate(text(), 'ACDORT', 'acdort'), 'add to cart') or contains(translate(@value, 'ACDORT', 'acdort'), 'add to cart') or contains(translate(@aria-label, 'ABDGOT', 'abdgot'), 'add to bag')]"
    ADD_TO_NEW_PAT = "//*[contains(translate(., 'ADTOBG', 'adtobg'), 'add to bag') or contains(translate(., 'ACDORT', 'acdort'), 'add to cart') or contains(translate(., 'SHOPNW', 'shopnw'), 'shop now')]"

class Scenario:
    LOGIN = "login"
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
