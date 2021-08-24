from modules import add_to_cart
from modules.add_to_cart import AddToCart
from behave import *

@given('url of product page to check add to cart')
def step_impl(context):
    add_to_cart = AddToCart(context)
    add_to_cart.find_add_to_()
    context.current_obj = add_to_cart

@when('add to cart found or check for overlays')
def step_impl(context):
    if (not context.current_obj.check_cookies_overlay()):
        if (not context.current_obj.is_closeable_overlay()):
            if (context.current_obj.required_element is None):
                context.scenario.skip(reason="Cannot find add to cart button.")

@then('we should proceed to checkout')
def step_impl(context):
    context.current_obj.hit_add_to_cart_element()