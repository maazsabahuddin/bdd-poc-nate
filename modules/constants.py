class Tags:
    BUTTON = "button"
    INPUT = "input"
    A = "a"
    SPAN = "span"
    POSSIBLE_BUY_TAGS_LIST = [BUTTON, INPUT, A, SPAN]
    POSSIBLE_ADDRESS_INPUT_TAGS_LIST = [INPUT]


class Pattern:
    BUY_PATTERN = "//*[contains(translate(text(), 'BUY', 'buy'), 'buy')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(translate(text(), 'ACEPT', 'acept'), 'accept') and contains(translate(text(), 'COKIES', 'cokies'), 'cookies') or contains(translate(@name, 'ACEPT', 'acept'), 'accept'))]"
    ADD_TO_PATTERN = "//*[contains(translate(text(), 'ABDGOT', 'abdgot'), 'add to bag') or contains(translate(text(), 'ACDORT', 'acdort'), 'add to cart') or contains(translate(@value, 'ACDORT', 'acdort'), 'add to cart') or contains(translate(@aria-label, 'ABDGOT', 'abdgot'), 'add to bag')]"
    ADD_TO_NEW_PAT = "//*[contains(translate(., 'ADTOBG', 'adtobg'), 'add to bag') or contains(translate(., 'ACDORT', 'acdort'), 'add to cart') or contains(translate(., 'SHOPNW', 'shopnw'), 'shop now')]"
    LOGIN_AS_GUEST_PATTERN = "//*[contains(translate(text(),'GUEST','guest'),'guest') or contains(translate(text(),'CONTINUE','continue'),'continue')]"
    SIGN_IN_PATTERN = "//*[contains(translate(text(),'SIGN','sign'),'sign-in')]"
    IS_CHECKOUT_PAGE_PATTERN = "//*[contains(translate(text(),'CHEKOUT','chekout'),'checkout') or contains(translate(text(),'ORDESUMAY','ordesumay'),'order summary') or contains(translate(text(),'YOURDE','yourde'),'your order')]"
    ADDRESS_PATTERN = "//*[contains(translate(text(), 'ADRES', 'adres'), 'adres')]"
    FIRST_NAME = "//input[contains(@name, 'FirstName') or contains(@name, 'firstName')]"
    LAST_NAME = "//input[contains(@name, 'LastName') or contains(@name, 'lastName')]"
    EMAIL = "//input[contains(@name, 'Email') or contains(@name, 'email')]"
    PREFIX = "//input[contains(@name, 'phones[0].countryCode')]"
    PHONE = "//input[contains(@name, 'Phone') or contains(@name, 'phones[0].subscriberNumber')]"
    ADDRESS1 = "//input[contains(@name, 'StreetLine1') or contains(@name, 'addressLines[0]')]"
    ADDRESS2 = "//input[contains(@name, 'StreetLine2') or contains(@name, 'addressLines[1]')]"
    CITY = "//input[contains(@name, 'AdministrativeArea') or contains(@name, 'city')]"
    # STATE = "//input[contains(@name, 'Municipality')]"
    STATE = "//select[contains(@name, 'stateCode')]"
    POSTAL_CODE = "//input[contains(@name, 'PostalCode') or contains(@name, 'zipCode')]"
    CONTINUE = "//*[contains(text()='Continue') or contains(text(),'CONTINUE')]"
    # COUNTRY = "//select[contains(@name, 'Country')]"

    POSSIBLE_BUY_TAGS_LIST = ["button", "input", "a", "span"]
    POSSIBLE_ADD_TO_TAGS_LIST = ["button", "span", "input"]
    POSSIBLE_LOGIN_AS_GUEST_LIST = ["button", "a"]
    POSSIBLE_SIGNIN_LIST = ["a"]
    POSSIBLE_CHECKOUT_PAGE_LIST = ["h1", "h2", "h3", "button"]


class SkipScenario:
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"


class ETC:
    VALUE = "value"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
