from modules.proceed_to_checkout_step1 import ProceedToCheckoutStep1
from behave import *

@given('In page, product is added into cart')
def step_impl(context):
    view_cart = ProceedToCheckoutStep1(context)
    view_cart.find_cart()
    context.current_obj = view_cart

@when('cart/check out button found')
def step_impl(context):
    if (context.current_obj.required_element is not None):
        pass
    else:
        context.scenario.skip(reason="Required button not found.")

@then('Click to proceed')
def step_impl(context):
    context.current_obj.hit_button_to_proceed()