# Framework imports
from behave import *

# Local imports
from file import close_file
from modules.shipping_info import Shipping
from utility.constants import ETC
from app import _result_file


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
    if context.current_obj.validate_fields():
        pass
    else:
        context.scenario.skip(reason="Required fields not found.")


@then('Enter shipping address details and proceed')
def proceed_shipping_address_page(context):
    """
    Enter details and proceed to checkout
    :param context:
    """
    context.current_obj.fill_out_data()
    context.current_obj.click_now()
    if not context._root[ETC.IS_CASE_FAILED]:
        _result_file.write(f"{context.name} - PASSED\n") if context.log == "True" else None
        close_file(_result_file)
