# Framework imports
import time

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
    if not context.current_obj.is_add_to_cart_found and not context.current_obj.is_cart_flow:
        context.current_obj.web.skip_all_remaining_scenarios()


@then('click on add to cart and proceed to next step')
def step_impl(context):
    if context.current_obj.is_cart_flow:
        context.current_obj.cart_flow_()
    else:
        context.current_obj.select_color_size()
        context.current_obj.hit_add_to_cart_element()
