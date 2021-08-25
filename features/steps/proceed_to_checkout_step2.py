from modules.proceed_to_checkout_step2 import ProceedToCheckoutStep2
from behave import *

@given('In page, product is added into cart')
def step_impl(context):
    cart_checkout = ProceedToCheckoutStep2(context)
    cart_checkout.find_cart_checkout()
    context.current_obj = cart_checkout

@when('Checkout button is found')
def step_impl(context):
    if (context.current_obj.required_element is not None):
        pass
    else:
        context.scenario.skip(reason="Required button not found.")

@then('Click to proceed')
def step_impl(context):
    context.current_obj.hit_button_to_proceed()