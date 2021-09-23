# Framework imports
from behave import *

# Local imports
from modules.proceed_to_checkout_step2 import ProceedToCheckoutStep2
from app import _result_file
from utility.constants import ETC

@given('product detailed page')
def step_impl(context):
    cart_checkout = ProceedToCheckoutStep2(context)
    cart_checkout.find_cart_checkout()
    context.current_obj = cart_checkout


@when('checkout or proceed to checkout button found')
def step_impl(context):
    if context.current_obj.required_element is not None:
        pass
    else:
        context.scenario.skip(reason="Required button not found.")


@then('click to move further')
def step_impl(context):
    context.current_obj.hit_button_to_proceed()
    if not context._root[ETC.IS_CASE_FAILED]:
        _result_file.write(f"proceed_to_checkout_2--->{context.name},") if context.log == "True" else None
