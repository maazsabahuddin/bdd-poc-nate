from modules import add_to_cart
from modules.add_to_cart import AddToCart
from behave import *

@given('url of buy now page')
def step_impl(context):
    print("In add to cart senario")
    add_to_cart = AddToCart(context)
    add_to_cart.find_add_to_()

@then('we should proceed to login page')
def step_impl(context):
    print("In add to cart then")