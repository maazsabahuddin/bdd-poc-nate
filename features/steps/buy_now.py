from behave import *
from modules.buy_now import BuyNow
from modules.constants import Scenario

@given('url of product page')
def step_impl(context):
    # create a object
    buy_now = BuyNow(context)
    buy_now.check_buy_now_page()

@when('buy now found')
def step_impl(context):
    if (context.move_to_login):
        context.web.skip_scenario(Scenario.SKIP_ADD_TO_CART)
    else:
        context.scenario.skip(reason='we found the add to cart button')

@then('click on buy now and proceed to next step')
def step_impl(context):
    '''logic to detect its a valid login page'''
    if (context.move_to_login):
        print("Login page")
    else:
        print("buy now not found move to next senario to find add to ... button")