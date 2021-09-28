class Tags:

    BUTTON = "button"
    INPUT = "input"
    A = "a"
    SPAN = "span"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    DIV = "div"
    SELECT = "select"


class TagsList:

    POSSIBLE_BUY_TAGS_LIST = [Tags.BUTTON, Tags.INPUT, Tags.A, Tags.SPAN]
    POSSIBLE_ADDRESS_INPUT_TAGS_LIST = [Tags.INPUT]
    POSSIBLE_VIEW_CART = [Tags.BUTTON, Tags.INPUT, Tags.A, Tags.DIV]
    POSSIBLE_ADD_TO_TAGS_LIST = [Tags.BUTTON, Tags.SPAN, Tags.INPUT, Tags.DIV]
    POSSIBLE_LOGIN_AS_GUEST_LIST = [Tags.BUTTON, Tags.A]
    POSSIBLE_SIGNIN_LIST = [Tags.A]
    POSSIBLE_CHECKOUT_PAGE_LIST = [Tags.H1, Tags.H2, Tags.H3, Tags.BUTTON]
    POSSIBLE_INPUT_ELEMENT = [Tags.INPUT]
    POSSIBLE_CONTINUE_BUTTON = [Tags.BUTTON, Tags.A, Tags.SPAN]
    POSSIBLE_CONFIRM_AND_PAY_ELEMENTS = [Tags.BUTTON, Tags.A, Tags.SPAN]
    POSSIBLE_CARD_ELEMENTS = [Tags.INPUT, Tags.SELECT, Tags.SPAN]
    POSSIBLE_COOKIES_ELEMENTS = [Tags.BUTTON, Tags.A]
    POSSIBLE_CARD_TYPE_ELEMENTS = [Tags.INPUT, Tags.SELECT, Tags.BUTTON, Tags.DIV, Tags.SPAN]


class Pattern:

    BUY_PATTERN = "//*[contains(translate(text(), 'BUY', 'buy'), 'buy') " \
                  "or contains(translate(@value, 'BUY', 'buy'), 'buy')]"
    ADD_TO_PATTERN = "//*[contains(translate(text(), 'ABDGOT', 'abdgot'), 'add to bag') " \
                     "or contains(translate(text(), 'ACDORT', 'acdort'), 'add to cart') " \
                     "or contains(translate(@value, 'ACDORT', 'acdort'), 'add to cart') " \
                     "or contains(translate(@aria-label, 'ABDGOT', 'abdgot'), 'add to bag') " \
                     "or contains(translate(text(), 'ADD', 'add'), 'add') " \
                     "or contains(normalize-space(translate(@name, 'ABDGOT', 'abdgot')), 'addtobag') " \
                     "or contains(translate(@name, 'ADD', 'add'), 'add')]"
    VIEW_CART = "//*[contains(translate(., 'VIEWBAG', 'viewbag'), 'view bag') " \
                "or contains(translate(text(), 'CHEKOUT', 'chekout'), 'checkout') " \
                "or contains(translate(text(), 'CHEKOUT', 'chekout'), 'check out') " \
                "or text()='Cart' " \
                "or contains(translate(., 'PROCEDTHKU', 'procedthku'), 'proceed to checkout') " \
                "or contains(translate(text(), 'SHOPINGA', 'shopinga'), 'shopping bag') " \
                "or contains(translate(@class, 'MYCART', 'mycart'), 'mycart') " \
                "or contains(translate(@id, 'CARTBUON', 'cartbuon'), 'cartbutton') " \
                "or contains(translate(text(), 'GOTCAR', 'gotcar'), 'go to cart') " \
                "or contains(translate(@class, 'CARTDOPWN', 'cartdopwn'), 'cart dropdown')]"
    LOGIN_AS_GUEST_PATTERN = "//*[contains(translate(text(),'GUEST','guest'),'guest') " \
                             "or contains(translate(text(),'CONTINUE','continue'),'continue')]"
    SIGN_IN_PATTERN = "//*[contains(translate(text(),'SIGN','sign'),'sign-in')]"
    IS_CHECKOUT_PAGE_PATTERN = "//*[contains(translate(text(),'CHEKOUT','chekout'),'checkout') " \
                               "or contains(translate(text(),'ORDESUMAY','ordesumay'),'order summary') " \
                               "or contains(translate(text(),'YOURDE','yourde'),'your order')]"
    ADDRESS_PATTERN = "//*[contains(translate(text(), 'ADRES', 'adres'), 'adres')]"
    VIEW_CART_CHECKOUT = "//*[contains(translate(text(), 'CHEKOUT', 'chekout'), 'checkout') " \
                         "or contains(translate(text(), 'CONTIUE', 'contiue'), 'continue') " \
                         "or contains(translate(., 'PROCEDTHKU', 'procedthku'), 'proceed to checkout') "\
                         "or contains(translate(@name, 'CHEKOUT', 'chekout'), 'checkout')]"
    ENTER_ADDRESS = "//div[contains(translate(text(), 'ENTR ADRES', 'Entr adres'), 'Enter address')]"
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
    FULL_NAME = "//input[contains(translate(@name, 'FULNAME-_', 'fulname-_'), 'fullname')]"
    EMAIL = "//input[contains(translate(@name, 'EMAIL-_[]', 'email-_[]'), 'email') " \
            "or contains(translate(@id, 'EMAIL-_[]', 'email-_[]'), 'email')]"
    COUNTRY_CODE = "//input[contains(@name, 'countryCode')]"
    PHONE = "//input[contains(translate(@name, 'TELEPHONE-_', 'telephone-_'), 'telephone') " \
            "or contains(@name, 'phones[0].subscriberNumber') or contains(@name, 'phoneNumber') " \
            "or contains(@name, 'billing_phone') or contains(translate(@name, 'Number', 'number'), 'number') " \
            "or contains(translate(@name, 'PHONE', 'phone'), 'phone') " \
            "or contains(@name, 'primaryVoiceNumber') " \
            "or contains(@id, 'phones[0].subscriberNumber') or contains(@id, 'phoneNumber') " \
            "or contains(@id, 'billing_phone') or contains(@id, 'primaryVoiceNumber') " \
            "or contains(@aria-label, 'Phone Number')]"
    ADDRESS1 = "//input[contains(@name, 'StreetLine1') or contains(@name, 'addressLines[0]') " \
               "or contains(@name, 'shipping-street-address') or contains(@name, 'addressLineOne') " \
               "or contains(@name, 'addressLine1') or contains(@name, 'addr1') or contains(@id, 'StreetLine1') " \
               "or contains(translate(@name, 'ADDRESS1', 'address1'), 'address') " \
               "or contains(@name, 'billing_address_1') or contains(translate(@name, 'LINE1', 'line1'), 'line1') " \
               "or contains(@id, 'addressLines[0]') or contains(@id, 'shipping-street-address') " \
               "or contains(@id, 'addressLineOne') or contains(@id, 'addressLine1') or contains(@id, 'street1') " \
               "or contains(translate(@id, 'ADRES1', 'adres1'), 'address1') " \
               "or contains(translate(@id, 'ADRES-1', 'adres-1'), 'address-1')]"
    ADDRESS2 = "//input[contains(@name, '2') or contains(@name, 'StreetLine2') or contains(@name, 'addressLines[1]') " \
               "or contains(@name, 'addressLineTwo') or contains(@name, 'addr2') or contains(@name, 'addressLine2') " \
               "or contains(translate(@name, 'APARTMENT', 'apartment'), 'apt') " \
               "or contains(@name, 'billing_address_2') or contains(translate(@name, 'LINE2', 'line2'), 'line2') " \
               "or contains(@id, 'StreetLine2') or contains(@id, 'addressLines[1]') " \
               "or contains(@id, 'addressLineTwo') or contains(@id, 'addressLine2') " \
               "or contains(translate(@id, 'ADRES2', 'adres2'), 'address2')]"
    CITY = "//input[contains(@name, 'AdministrativeArea') or contains(translate(@name, 'CITY', 'city'), 'city') " \
           "or contains(@id, 'AdministrativeArea') or contains(translate(@id, 'CITY', 'city'), 'city') " \
           "or contains(translate(@name, 'LOCALITY', 'locality'), 'locality') " \
           "or contains(translate(@name, 'TOWN', 'town'), 'town')]"
    STATE = "//select[contains(@name, 'stateCode') or contains(@name, 'state') or contains(@name, 'region') " \
            "or contains(@id, 'stateCode') or contains(@id, 'state') or contains(@id, 'region') " \
            "or contains(translate(@name, 'PROVINCE', 'province'), 'province')] | " \
            "//input[contains(@name, 'stateCode') or contains(translate(@name, 'STATE', 'state'), 'state') " \
            "or contains(@name, 'region') or contains(@id, 'stateCode') or contains(@id, 'state') " \
            "or contains(@id, 'region')]"
    POSTAL_CODE = "//input[contains(@name, 'postal') or contains(translate(@name, 'ZIP', 'zip'), 'zip') " \
                  "or contains(@name, 'shipping-zip-code') or contains(@name, 'postcode') " \
                  "or contains(@id, 'postal') or contains(@id, 'zip') or contains(@id, 'postcode') " \
                  "or contains(@id, 'shipping-zip-code')]"
    COUNTRY = "//select[contains(translate(@name, 'COUNTRY', 'country'), 'country')]"
    CONTINUE = "//*[contains(text(), 'Continue') or contains(text(), 'CONTINUE') or contains(text(), 'next') " \
               "or contains(translate(text(), 'DONE', 'done'), 'done') " \
               "or contains(translate(text(), 'PROCEDTHKU', 'procedthku'), 'proceed to checkout') " \
               "or contains(translate(text(), 'SUBMIT', 'submit'), 'submit') " \
               "or contains(translate(text(), 'SAVE', 'save'), 'save')] | " \
               "//button[contains(@type, 'submit') and contains(translate(text(), 'SHIP', 'ship'), 'ship')]"
    PLACE_ORDER = "//*[contains(@name, 'place')]"
    CONSENT = "//input[contains(@type, 'checkbox')]"

    GUEST_BUTTON = "//*[contains(translate(text(),'CONTINUE','continue'),'continue') " \
                   "or contains(translate(text(),'GUEST','guest'),'guest') " \
                   "or contains(translate(text(), 'SAVE', 'save'), 'save') " \
                   "or contains(translate(text(), 'ADEILMY', 'adeilmy'), 'add my email')]"
    CONFIRM_AND_PAY = "//*[contains(translate(text(), 'PLACEORD', 'placeord'), 'place order') or " \
                      "contains(translate(text(), 'AUTHORIZEPYMN', 'authorizepymn'), 'authorize payment') or " \
                      "contains(translate(text(), 'SUBMITORDER', 'submitorder'), 'submit order') or " \
                      "contains(translate(text(), 'COMPLETPURHAS', 'completpurhas'), 'complete purchase')]"
    PLACE_ORDER_BUTTON = "//button[contains(translate(text(), 'PLACEORD', 'placeord'), 'place order')]"
    REVIEW_ORDER = "//*[contains(translate(text(), 'REVIW', 'reviw'), 'review') " \
                   "and contains(translate(text(), 'ORDE', 'orde'), 'order')]"

    # Card details
    CARD_NUMBER = "//input[contains(translate(@name, 'CARD', 'card'), 'card') " \
                  "and contains(translate(@name, 'NUM', 'num'), 'num') " \
                  "or contains(translate(@id, 'CARD', 'card'), 'card') and " \
                  "contains(translate(@id, 'NUM', 'num'), 'num') " \
                  "or contains(translate(@name, 'CREDITAD', 'creditad'), 'creditcard') " \
                  "or contains(translate(@id, 'INPUT', 'input'), 'input') " \
                  "and contains(translate(@id, 'NUMBER', 'number'), 'number') " \
                  "or @autocomplete ='cc-number' " \
                  "or @name = 'pan']"
    EXPIRATION_MONTH = "//*[contains(translate(@id, 'EXPMONTH', 'expmonth'), 'expmonth') " \
                       "or contains(translate(@name, 'EXPDAT', 'expdat'), 'expdate') " \
                       "or contains(translate(@name, 'EXPDAT', 'expdat'), 'exp-date') " \
                       "or contains(translate(@placeholder, 'MY', 'my'), 'mm/yy') " \
                       "or contains(translate(@id, 'EXPIRATON', 'expiraton'), 'expiration') " \
                       "or contains(translate(@id, 'MONTH', 'month'), 'month') " \
                       "or contains(translate(@name, 'MONTH', 'month'), 'month') " \
                       "or contains(translate(@id, 'EXP', 'exp'), 'exp') " \
                       "or @autocomplete = 'cc-exp-month' " \
                       "or contains(translate(@name, 'EXPIRATOND', 'expiratond'), 'expirationdate')]"
    EXPIRATION_YEAR = "//*[contains(translate(@id, 'EXPYAR', 'expyar'), 'expyear') " \
                      "or contains(translate(@name, 'EXPYAR', 'expyar'), 'expyear') " \
                      "or contains(translate(@name, 'EXPYAR', 'expyar'), 'exp-year') " \
                      "or contains(translate(@id, 'YEAR', 'year'), 'year') " \
                      "or contains(translate(@name, 'YEAR', 'year'), 'year') " \
                      "or @autocomplete = 'cc-exp-year']"
    CVV = "//input[contains(translate(@name, 'SECURITYOD', 'securityod'), 'securitycode') " \
          "or contains(translate(@name, 'CV', 'cv'), 'cv') " \
          "or contains(translate(@id, 'CVN', 'cvn'), 'cvn') " \
          "or contains(translate(@id, 'CV', 'cvv'), 'cvv') " \
          "or contains(translate(@id, 'SECURITYOD', 'securityod'), 'securitycode') " \
          "or contains(translate(@id, 'CARDOE', 'cardoe'), 'cardcode') " \
          "or contains(translate(@id, 'VALIDTONCE', 'validtonce'), 'validationcode')]"
    CARD_HOLDER_NAME = "//input[contains(translate(@id, 'NAME', 'name'), 'name') " \
                       "and contains(translate(@id, 'CARD', 'card'), 'card') " \
                       "or contains(translate(@name, 'HOLDER', 'holder'), 'holder') " \
                       "or contains(translate(@id, 'BILGNAME', 'bilgname'), 'billing-name') " \
                       "or contains(translate(@id, 'INPUTAME', 'inputame'), 'input-name')]"
    CARD_TYPE = "//*[contains(translate(@name, 'CARDTYPE', 'cardtype'), 'cardtype') " \
                "or contains(translate(text(), 'CREDIT', 'credit'), 'credit') " \
                "and contains(translate(text(), 'DEBIT', 'debit'), 'debit') " \
                "and contains(translate(text(), 'CARD', 'card'), 'card') " \
                "or contains(translate(@name, 'CREDITOPNS', 'creditopns'), 'creditoptions') " \
                "or contains(translate(text(), 'CREDITA', 'credita'), 'creditcard') " \
                "or contains(translate(@value, 'VISA', 'visa'), 'visa')]"
    # Cookies overlay
    ACCEPT_COOKIES_PATTERN = "//button[contains(translate(text(), 'ACEPT', 'acept'), 'accept')" \
                             "or contains(translate(@name, 'ACEPT', 'acept'), 'accept')" \
                             "or contains(translate(@id, 'ACEPTOKI', 'aceptoki'), 'acceptcookie')]" \
                             "| //a[contains(translate(text(), 'ACEPT', 'acept'), 'accept')]"

    # Promotion overlay
    PROMOTION_OVERLAY_PATTERN = "//button[contains(translate(@aria-label, 'CLOSE', 'close'), 'close') " \
                                "or contains(translate(@aria-label, 'CONFIRM', 'confirm'), 'confirm') " \
                                "or contains(translate(@class, 'PROM', 'prom'), 'promo')" \
                                "or contains(translate(text(), 'NOTHAKS', 'nothaks'), 'no thanks')" \
                                "or contains(translate(@class, 'CLOSEBUTN', 'closebutn'), 'closebutton') "\
                                "or contains(translate(@class, 'CLOSE', 'close'), 'close') " \
                                "or contains(translate(@class, 'OPENSTAGL', 'openstagl'), 'openstatetoggle')]" \
                                "| //div[contains(translate(@class, 'CLOSEMDAL', 'closemdal'), 'closemodal')" \
                                "or contains(translate(@class, 'CLOSEBUTN', 'closebutn'), 'closebutton') " \
                                "or contains(translate(text(), 'DECLINEA', 'declinea'), 'decline all')]" \
                                "| //a[contains(translate(@title, 'CLOSE', 'close'), 'close')]" \
                                "| //span[contains(translate(@class, 'ICONLSE', 'iconlse'), 'icon-close')]"

    # Keywords to check address details
    KeyWords = "//h2[contains(translate(text(), 'CONTAIFRM', 'contaifrm'), 'contact information') " \
               "or contains(translate(text(), 'SHIPNGADRES', 'shipngadrs'), 'shipping address') " \
               "or contains(translate(text(), 'DELIVRYTAIS', 'delivrytais'), 'delivery details')]" \
               "| //h4[contains(translate(text(), 'CONTAIFRM', 'contaifrm'), 'contact information') " \
               "or contains(translate(text(), 'SHIPNGADRES', 'shipngadrs'), 'shipping address')" \
               "or contains(translate(text(), 'DELIVRYTAIS', 'delivrytais'), 'delivery details')]"


class SkipScenario:

    SKIP_SCENARIO = "skip_scenario"
    SKIP_ALL = "skip_all"
    SKIP_LOGIN = "skip_login"
    SKIP_ADD_TO_CART = "skip_add_to_cart"
    SKIP_CHECKOUT_STEP_2 = "skip_checkout_step_2"
    SKIP_PROCEED_CHECKOUT = "skip_proceed_checkout"
    SKIP_PERSONAL_INFO = "skip_personal_info"


class ETC:

    VALUE = "value"
    NAME = "name"
    OPTION = "option"
    FAILED = "failed"
    TEXT = "text"
    LOG = "log"
    COLOR = "color"
    SIZE = "size"
    BEHAVE_DEBUG_ON_ERROR = "BEHAVE_DEBUG_ON_ERROR"
    URL = "url"
    IS_CASE_FAILED = "is_case_failed"


class UserInfo:

    # USER INFO CONSTANTS
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
    CARD_EXPIRATION_MONTH = "09"
    CARD_EXPIRATION_YEAR = "2022"
    CARD_TYPE = ["Visa", "MasterCard"]


class Timer:
    
    PAGE_LOAD_TIMEOUT = 120
    ELEMENT_TIMEOUT = 10
    PROCESS_PAUSE_TIMEOUT = 12
    ONE_SECOND_TIMEOUT = 1
    THREE_SECOND_TIMEOUT = 3
    FIVE_SECOND_TIMEOUT = 5
