class Tags:
    BUTTON = "button"
    INPUT = "input"
    A = "a"
    SPAN = "span"
    POSSIBLE_BUY_TAGS_LIST = [BUTTON, INPUT, A, SPAN]
    POSSIBLE_ADDRESS_INPUT_TAGS_LIST = [INPUT]


class Pattern:
    BUY_PATTERN = "//*[contains(text(),'Buy') or contains(text(),'BUY')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(text(),'Accept') and contains(text(),'Cookies')) or " \
                             "(contains(text(),'Accept') and contains(text(),'cookies')) or " \
                             "(contains(text(),'accept') and contains(text(),'cookies'))]"
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


class Scenarios:
    LOGIN = "login"
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"


class ETC:
    VALUE = "value"
