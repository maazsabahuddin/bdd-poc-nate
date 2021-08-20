from behave import *
from modules.buy_now import BuyNow
from modules.constants import Scenario

@given('url of product page')
def step_impl(context):
    # create a object
    buy_now = BuyNow(context)
    buy_now.check_buy_now_page()

@then('we should land to login page')
def step_impl(context):
    '''logic to detect its a valid login page'''
    if (context.move_to_login):
        print("Login page")
    else:
        print("buy now not found move to next senario to find add to ... button")