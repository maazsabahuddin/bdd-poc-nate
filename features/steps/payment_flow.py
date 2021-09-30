# Framework imports
from behave import *

# Local imports
from modules.payment import Payment


@given('Payment Button')
def shipping_address_required_step(context):
    """
    Gather required elements
    :param context:
    """
    payment = Payment(context)
    payment.fetching_required_elements()
    context.current_obj = payment


@when('If payment button found')
def identify_scenario(context):
    """
    Check which type of page is identified and call that controller accordingly.
    :param context:
    """
    if not context.current_obj.validate_payment_fields():
        context.scenario.skip(reason='cannot find payment field')


@then('Click on it')
def proceed_shipping_address_page(context):
    """
    Enter details and proceed to checkout
    :param context:
    """
    context.current_obj.click_now()
