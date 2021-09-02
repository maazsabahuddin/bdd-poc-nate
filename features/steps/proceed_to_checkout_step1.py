# Framework imports
from behave import *

# Local imports
from modules.proceed_to_checkout_step1 import ProceedToCheckoutStep1


@given('In page, product is added into cart')
def step_impl(context):
    view_cart = ProceedToCheckoutStep1(context)
    view_cart.find_cart()
    context.current_obj = view_cart


@when('cart/check out button found')
def step_impl(context):
    if not context.current_obj.is_checkout_found:
        context.scenario.skip(reason="Required button not found.")


@then('Click to proceed')
def step_impl(context):
    context.current_obj.hit_button_to_proceed()
