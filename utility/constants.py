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
    FIRST_NAME = "//input[contains(translate(@name, 'FIRSTNAME-_', 'firstname-_'), 'firstname') " \
                 "or contains(@name, 'FirstName') or contains(@name, 'firstName') " \
                 "or contains(@name, 'billing_first_name') or contains(@name, 'shipping-first-name') " \
                 "or contains(@name, 'given-name') " \
                 "or contains(translate(@id, 'FIRSTNAME-_', 'firstname-_'), 'firstname') " \
                 "or contains(@id, 'FirstName') or contains(@id, 'firstName') or contains(@id, 'shipping-first-name')" \
                 "or contains(@id, 'billing_first_name')]"
    LAST_NAME = "//input[contains(translate(@name, 'LASTNAME-_', 'lastname-_'), 'lastname') " \
                "or contains(@name, 'LastName') or contains(@name, 'lastName') " \
                "or contains(@name, 'billing_last_name') or contains(@name, 'shipping-last-name') " \
                "or contains(@name, 'family-name') " \
                "or contains(@id, 'LastName') or contains(@id, 'lastName') or contains(@id, 'shipping-last-name') " \
                "or contains(@id, 'billing_last_name')]"
    FULL_NAME = "//input[contains(translate(@name, 'FULLNAME-_', 'fullname-_'), 'fullName') " \
                "or contains(translate(@id, 'FULLNAME-_', 'fullname-_'), 'fullName')]"
    # EMAIL = "//input[contains(@name, 'Email') or contains(@name, 'email') or contains(@name, 'contact-email')" \
    #         "or contains(@name, 'billing_email')" \
    #         "or contains(@id, 'Email') or contains(@id, 'email') or contains(@id, 'contact-email')" \
    #         "or contains(@id, 'billing_email')]"
    EMAIL = "//input[contains(translate(@name, 'EMAIL-_[]', 'email-_[]'), 'email') " \
            "or contains(translate(@id, 'EMAIL-_[]', 'email-_[]'), 'email')]"
    COUNTRY_CODE = "//input[contains(@name, 'countryCode')]"
    PHONE = "//input[contains(translate(@name, 'TELEPHONE-_', 'telephone-_'), 'telephone') " \
            "or contains(@name, 'phones[0].subscriberNumber') or contains(@name, 'phoneNumber') " \
            "or contains(@name, 'billing_phone') or contains(translate(@name, 'Number', 'number'), 'number') " \
            "or contains(translate(@name, 'Phone', 'phone'), 'phone')" \
            "or contains(@name, 'primaryVoiceNumber')" \
            "or contains(@id, 'phones[0].subscriberNumber') or contains(@id, 'phoneNumber') " \
            "or contains(@id, 'billing_phone') or contains(@id, 'primaryVoiceNumber') " \
            "or contains(@aria-label, 'Phone Number')]"
    ADDRESS1 = "//input[contains(@name, 'StreetLine1') or contains(@name, 'addressLines[0]') " \
               "or contains(@name, 'shipping-street-address') or contains(@name, 'addressLineOne') " \
               "or contains(@name, 'addressLine1') or contains(@id, 'StreetLine1') " \
               "or contains(translate(@name, 'ADDRESS', 'address'), 'address') " \
               "or contains(@name, 'billing_address_1') or contains(translate(@name, 'LINE1', 'line1'), 'line1') " \
               "or contains(@id, 'addressLines[0]') or contains(@id, 'shipping-street-address') " \
               "or contains(@id, 'addressLineOne') or contains(@id, 'addressLine1') or contains(@id, 'street1')]"
    ADDRESS2 = "//input[contains(@name, 'StreetLine2') or contains(@name, 'addressLines[1]') " \
               "or contains(@name, 'addressLineTwo') or contains(@name, 'addressLine2') " \
               "or contains(@name, 'billing_address_2') or contains(translate(@name, 'LINE2', 'line2'), 'line2') " \
               "or contains(@id, 'StreetLine2') or contains(@id, 'addressLines[1]') " \
               "or contains(@id, 'addressLineTwo') or contains(@id, 'addressLine2')]"
    CITY = "//input[contains(@name, 'AdministrativeArea') or contains(@name, 'city')" \
           "or contains(@id, 'AdministrativeArea') or contains(@id, 'city') " \
           "or contains(translate(@name, 'TOWN', 'town'), 'town')]"
    STATE = "//select[contains(@name, 'stateCode') or contains(@name, 'state') or contains(@name, 'region')" \
            "or contains(@id, 'stateCode') or contains(@id, 'state') or contains(@id, 'region') " \
            "or contains(translate(@name, 'PROVINCE', 'province'), 'province')] | " \
            "//input[contains(@name, 'stateCode') or contains(@name, 'state') or contains(@name, 'region')" \
            "or contains(@id, 'stateCode') or contains(@id, 'state') or contains(@id, 'region')]"
    POSTAL_CODE = "//input[contains(@name, 'postal') or contains(@name, 'zip') " \
                  "or contains(@name, 'shipping-zip-code') or contains(@name, 'postcode') " \
                  "or contains(@id, 'postal') or contains(@id, 'zip') or contains(@id, 'postcode') " \
                  "or contains(@id, 'shipping-zip-code')]"
    COUNTRY = "//select[contains(@name, 'Country') or contains(@name, 'shipping-country') " \
              "or contains(@name, 'country')]"
    CONTINUE = "//*[contains(text(), 'Continue') or contains(text(), 'CONTINUE') or contains(text(), 'next') " \
               "or contains(text(), 'done') " \
               "or contains(translate(text(), 'PROCEED CHECKOUT', 'proceed checkout'), 'proceed to checkout') " \
               "or contains(translate(text(), 'SAVE', 'save'), 'save')] | " \
               "//button[contains(@type, 'submit') and contains(translate(text(), 'SHIP', 'ship'), 'ship')]"
    # CONTINUE = "//*[contains(translate(text(), 'PROCEED CHECKOUT', 'proceed checkout'), 'proceed to checkout')]"
    PLACE_ORDER = "//*[contains(@name, 'place')]"
    CONSENT = "//input[contains(@type, 'checkbox')]"


class SkipScenario:
    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
    SKIP_PROCEED_CHECKOUT = "skip_proceed_checkout"


class ETC:
    VALUE = "value"

    # SHIPPING INFO CONSTANTS
    FULL_NAME = "full_name"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    PHONE = "phone"
    EMAIL = "email"
    COUNTRY = "country"
    CITY = "city"
    ADDRESS1 = "address1"
    ADDRESS2 = "address2"
    STATE = "state"
    COUNTRY_CODE = "country_code"
    POSTAL_CODE = "postal_code"
    CONTINUE = "continue"
    CONSENT = "consent"


class Timer:
    PAGE_LOAD_TIMEOUT = 30
    ELEMENT_TIMEOUT = 10
    PROCESS_PAUSE_TIMEOUT = 5
