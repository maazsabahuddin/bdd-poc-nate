# Framework imports
from behave import *

# Local imports
from modules.buy_now import BuyNow


@given('Is shipping address page')
def shipping_address_step(context):
    """
    Check and verify if it is a shipping address page or not
    :param context:
    """
    pass


@then('enter details and proceed')
def proceed_shipping_address_page(context):
    """
    Enter details and proceed to checkout
    :param context:
    """
    pass
