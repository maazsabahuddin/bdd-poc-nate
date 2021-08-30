class Tags:

    BUTTON = "button"
    INPUT = "input"
    A = "a"
    SPAN = "span"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    DIV = "div"
    POSSIBLE_BUY_TAGS_LIST = [BUTTON, INPUT, A, SPAN]
    POSSIBLE_ADDRESS_INPUT_TAGS_LIST = [INPUT]
    POSSIBLE_ADD_TO_TAGS_LIST = [BUTTON, SPAN, INPUT]
    POSSIBLE_LOGIN_AS_GUEST_LIST = [BUTTON, A]
    POSSIBLE_SIGNIN_LIST = [A]
    POSSIBLE_CHECKOUT_PAGE_LIST = [H1, H2, H3, BUTTON]
    POSSIBLE_CONTINUE_BUTTON = [BUTTON, SPAN]


class Pattern:
    BUY_PATTERN = "//*[contains(translate(text(), 'BUY', 'buy'), 'buy') " \
                  "or contains(translate(@value, 'BUY', 'buy'), 'buy')]"
    ACCEPT_COOKIES_PATTERN = "//*[(contains(translate(text(), 'ACEPT', 'acept'), 'accept') " \
                             "and contains(translate(text(), 'COKIES', 'cokies'), 'cookies') " \
                             "or contains(translate(@name, 'ACEPT', 'acept'), 'accept'))]"
    ADD_TO_PATTERN = "//*[contains(translate(text(), 'ABDGOT', 'abdgot'), 'add to bag') " \
                     "or contains(translate(text(), 'ACDORT', 'acdort'), 'add to cart') " \
                     "or contains(translate(@value, 'ACDORT', 'acdort'), 'add to cart') " \
                     "or contains(translate(@aria-label, 'ABDGOT', 'abdgot'), 'add to bag')]"
    ADD_TO_NEW_PAT = "//*[contains(translate(., 'ADTOBG', 'adtobg'), 'add to bag') " \
                     "or contains(translate(., 'ACDORT', 'acdort'), 'add to cart') " \
                     "or contains(translate(., 'SHOPNW', 'shopnw'), 'shop now') " \
                     "or contains(text(), 'ADD')]"
    VIEW_CART = "//*[contains(translate(text(), 'VIEWBAG', 'viewbag'), 'view bag') " \
                "or contains(translate(text(), 'CHEKOUT', 'chekout'), 'checkout') " \
                "or contains(translate(text(), 'CHEKOUT', 'chekout'), 'check out') " \
                "or text()='Cart' or contains(translate(text(), 'PROCEDTHKU', 'procedthku'), 'proceed to checkout') " \
                "or contains(translate(text(), 'SHOPINGA', 'shopinga'), 'shopping bag')]"
    LOGIN_AS_GUEST_PATTERN = "//*[contains(translate(text(),'GUEST','guest'),'guest') " \
                             "or contains(translate(text(),'CONTINUE','continue'),'continue')]"
    SIGN_IN_PATTERN = "//*[contains(translate(text(),'SIGN','sign'),'sign-in')]"
    IS_CHECKOUT_PAGE_PATTERN = "//*[contains(translate(text(),'CHEKOUT','chekout'),'checkout') " \
                               "or contains(translate(text(),'ORDESUMAY','ordesumay'),'order summary') " \
                               "or contains(translate(text(),'YOURDE','yourde'),'your order')]"
    ADDRESS_PATTERN = "//*[contains(translate(text(), 'ADRES', 'adres'), 'adres')]"
    FIRST_NAME = "//input[contains(@name, 'FirstName') or contains(@name, 'firstName') " \
                 "or contains(@name, 'shipping-first-name')]"
    LAST_NAME = "//input[contains(@name, 'LastName') or contains(@name, 'lastName') " \
                "or contains(@name, 'shipping-last-name')]"
    EMAIL = "//input[contains(@name, 'Email') or contains(@name, 'email') or contains(@name, 'contact-email')]"
    PREFIX = "//input[contains(@name, 'phones[0].countryCode')]"
    PHONE = "//input[contains(@name, 'Phone') or contains(@name, 'phones[0].subscriberNumber') " \
            "or contains(@name, 'phoneNumber')]"
    ADDRESS1 = "//input[contains(@name, 'StreetLine1') or contains(@name, 'addressLines[0]') or " \
               "contains(@name, 'shipping-street-address')]"
    ADDRESS2 = "//input[contains(@name, 'StreetLine2') or contains(@name, 'addressLines[1]')]"
    CITY = "//input[contains(@name, 'AdministrativeArea') or contains(@name, 'city')]"
    STATE = "//select[contains(@name, 'stateCode') or contains(@name, 'state') or contains(@id, 'state')]"
    POSTAL_CODE = "//input[contains(@name, 'PostalCode') or contains(@name, 'zipCode') " \
                  "or contains(@name, 'shipping-zip-code')]"
    CONTINUE = "//*[contains(text(), 'Continue') or contains(text(), 'CONTINUE') " \
               "or contains(text(), 'next') or contains(text(), 'done') " \
               "or contains(text(), 'proceed')]"
    # CONTINUE = "//*[contains(text(), 'Go to next step')]"
    COUNTRY = "//select[contains(@name, 'Country') or contains(@name, 'shipping-country')]"


class SkipScenario:
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
    SKIP_PROCEED_CHECKOUT = "skip_proceed_checkout"


class ETC:
    VALUE = "value"


class Timer:
    PAGE_LOAD_TIMEOUT = 30
    ELEMENT_TIMEOUT = 10
    PROCESS_PAUSE_TIMEOUT = 5
