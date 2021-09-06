# Framework imports
from behave import *

# Local imports
from modules.add_to_cart import AddToCart


@given('url of product page to check add to cart')
def step_impl(context):
    add_to_cart = AddToCart(context)
    add_to_cart.find_add_to_()
    context.current_obj = add_to_cart


@when('add to cart found')
def step_impl(context):
    if not context.current_obj.is_add_to_cart_found:
        context.current_obj.web.skip_all_remaining_scenarios()
        context.scenario.skip(reason="Cannot find add to cart button.")


@then('click on add to cart and proceed to next step')
def step_impl(context):
    context.current_obj.hit_add_to_cart_element()
