class Tags:
    POSSIBLE_BUY_TAGS_LIST = ["button", "input", "a", "span"]
    POSSIBLE_ADD_TO_TAGS_LIST = ["button", "span", "input"]
    POSSIBLE_VIEW_CART = ["a", "button", "span"]
    POSSIBLE_LOGIN_AS_GUEST_LIST = ["button", "a"]
    POSSIBLE_SIGNIN_LIST = ["a"]
    POSSIBLE_CHECKOUT_PAGE_LIST = ["h1", "h2", "h3", "button"]

class Pattern:
    BUY_PATTERN = "//*[contains(translate(text(), 'BUY', 'buy'), 'buy') or contains(translate(@value, 'BUY', 'buy'), 'buy')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(translate(text(), 'ACEPT', 'acept'), 'accept') and contains(translate(text(), 'COKIES', 'cokies'), 'cookies') or contains(translate(@name, 'ACEPT', 'acept'), 'accept'))]"
    ADD_TO_PATTERN = "//*[contains(translate(text(), 'ABDGOT', 'abdgot'), 'add to bag') or contains(translate(text(), 'ACDORT', 'acdort'), 'add to cart') or contains(translate(@value, 'ACDORT', 'acdort'), 'add to cart') or contains(translate(@aria-label, 'ABDGOT', 'abdgot'), 'add to bag')]"
    ADD_TO_NEW_PAT = "//*[contains(translate(., 'ADTOBG', 'adtobg'), 'add to bag') or contains(translate(., 'ACDORT', 'acdort'), 'add to cart') or contains(translate(., 'SHOPNW', 'shopnw'), 'shop now') or contains(text(), 'ADD')]"
    VIEW_CART = "//*[contains(translate(text(), 'VIEWBAG', 'viewbag'), 'view bag') or contains(translate(text(), 'CHEKOUT', 'chekout'), 'checkout') or contains(translate(text(), 'CHEKOUT', 'chekout'), 'check out') or text()='Cart' or contains(translate(text(), 'PROCEDTHKU', 'procedthku'), 'proceed to checkout') or contains(translate(text(), 'SHOPINGA', 'shopinga'), 'shopping bag')]"
    LOGIN_AS_GUEST_PATTERN = "//*[contains(translate(text(),'GUEST','guest'),'guest') or contains(translate(text(),'CONTINUE','continue'),'continue')]"
    SIGN_IN_PATTERN = "//*[contains(translate(text(),'SIGN','sign'),'sign-in')]"
    IS_CHECKOUT_PAGE_PATTERN = "//*[contains(translate(text(),'CHEKOUT','chekout'),'checkout') or contains(translate(text(),'ORDESUMAY','ordesumay'),'order summary') or contains(translate(text(),'YOURDE','yourde'),'your order')]"

class SkipScenario:
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
    SKIP_PROCEED_CHECKOUT = "skip_proceed_checkout"