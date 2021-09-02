# Framework imports
from behave import *

# Local imports
from modules.ship import Shipping


@given('Shipping information required page')
def shipping_address_required_step(context):
    """
    Gather required elements
    :param context:
    """
    ship = Shipping(context)
    ship.fetching_required_elements()
    context.this = ship


@when('Shipping information found or not')
def identify_scenario(context):
    """
    Check which type of page is identified and call that controller accordingly.
    :param context:
    """
    if context.this.validate_fields():
        pass
    else:
        pass


@then('Enter shipping address details and proceed')
def proceed_shipping_address_page(context):
    """
    Enter details and proceed to checkout
    :param context:
    """
    context.this.fill_out_data()
    context.this.click_now()
