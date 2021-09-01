# Framework imports
from behave import *

# Local imports
from modules.ship import Shipping


@given('Find type of shipping address page')
def shipping_address_step(context):
    """
    Check and verify if it is a shipping address page or not
    :param context:
    """
    ship = Shipping(context)
    ship.login_flow = True
    ship.fetching_required_elements()
    ship.fill_out_data()
    ship.click_now()


@when('Shipping page ask about shipping address details')
def identify_scenario(context):
    """
    Check which type of page is identified and call that controller accordingly.
    :param context:
    """
    pass


@then('Enter shipping address details and proceed')
def proceed_shipping_address_page(context):
    """
    Enter details and proceed to checkout
    :param context:
    """
    pass
