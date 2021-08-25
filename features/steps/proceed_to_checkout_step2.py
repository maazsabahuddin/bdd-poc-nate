from modules.proceed_to_checkout_step2 import ProceedToCheckoutStep2
from behave import *

@given('product detailed page')
def step_impl(context):
    cart_checkout = ProceedToCheckoutStep2(context)
    cart_checkout.find_cart_checkout()
    context.current_obj = cart_checkout

@when('checkout or proceed to checkout button found')
def step_impl(context):
    if (context.current_obj.required_element is not None):
        pass
    else:
        context.scenario.skip(reason="Required button not found.")

@then('click to move futher')
def step_impl(context):
    context.current_obj.hit_button_to_proceed()