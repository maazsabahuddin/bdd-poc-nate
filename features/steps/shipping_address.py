# Framework imports
from behave import *

# Local imports
from features.environment import failed_case
from modules.shipping_info import Shipping


@given('Shipping information required page')
def shipping_address_required_step(context):
    """
    Gather required elements
    :param context:
    """
    ship = Shipping(context)
    ship.fetching_required_elements()
    context.current_obj = ship


@when('Shipping information found or not')
def identify_scenario(context):
    """
    Check which type of page is identified and call that controller accordingly.
    :param context:
    """
    if not context.current_obj.validate_fields():
        failed_case(scenario="Shipping Address", exception_message="Required fields not found.")


@then('Enter shipping address details and proceed')
def proceed_shipping_address_page(context):
    """
    Enter details and proceed to checkout
    :param context:
    """
    context.current_obj.fill_out_data()
    context.current_obj.click_now()
