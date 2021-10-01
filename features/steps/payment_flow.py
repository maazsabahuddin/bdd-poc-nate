# Framework imports
from behave import *

# Local imports
from modules.continuetopayment import ContinueToPayment
from utility.constants import ETC
from app import _result_file
from file import close_file


@given('Payment Button')
def step_impl(context):
    """
    Gather required elements
    :param context:
    """
    payment = ContinueToPayment(context)
    payment.fetching_required_elements()
    context.current_obj = payment


@when('If payment button found')
def step_impl(context):
    """
    Check which type of page is identified and call that controller accordingly.
    :param context:
    """
    if not context.current_obj.validate_payment_fields():
        context.scenario.skip(reason='cannot find payment field')


@then('Click on it')
def step_impl(context):
    """
    Enter details and proceed to checkout
    :param context:
    """
    context.current_obj.click_payment_button()
