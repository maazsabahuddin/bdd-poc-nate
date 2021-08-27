from behave import *
# Local imports
from modules.proceed_to_checkout import ProceedToCheckout

@given('In page, product is added into cart')
def step_impl(context):
    view_cart = ProceedToCheckout(context)
    view_cart.find_cart()
    context.current_obj = view_cart

@when('Checkout button is found')
def step_impl(context):
    if (context.current_obj.required_element is not None):
        pass
    else:
        context.scenario.skip(reason="Required button not found.")

@then('Click to proceed')
def step_impl(context):
    context.current_obj.hit_button_to_proceed()