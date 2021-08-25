class Tags:
    BUTTON = "button"
    INPUT = "input"
    A = "a"
    SPAN = "span"
    POSSIBLE_BUY_TAGS_LIST = [BUTTON, INPUT, A, SPAN]


class Pattern:
    BUY_PATTERN = "//*[contains(text(),'Buy') or contains(text(),'BUY')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(text(),'Accept') and contains(text(),'Cookies')) or " \
                             "(contains(text(),'Accept') and contains(text(),'cookies')) or " \
                             "(contains(text(),'accept') and contains(text(),'cookies'))]"
    ADDRESS_PATTERN = "//*[contains(translate(text(), 'ADRES', 'adres'), 'adres')]"
    FIRST_NAME = "x(//input[contains(@name, 'FirstName')])"
    LAST_NAME = "x(//input[contains(@name, 'LastName')])"
    EMAIL = "x(//input[contains(@name, 'Email')])"
    PHONE = "x(//input[contains(@name, 'Phone')])"
    ADDRESS1 = "x(//input[contains(@name, 'StreetLine1')])"
    ADDRESS2 = "x(//input[contains(@name, 'StreetLine2')])"
    CITY = "x(//input[contains(@name, 'AdministrativeArea')])"
    STATE = "x(//input[contains(@name, 'Municipality')])"
    POSTAL_CODE = "x(//input[contains(@name, 'PostalCode')])"
    # COUNTRY = "x(//select[contains(@name, 'Country')])"


class Scenarios:
    LOGIN = "login"
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
