from behave import *
from modules.buy_now import BuyNow

@given('url of buy now page')
def step_impl(context):
    # create a object
    buy_now = BuyNow(context)
    buy_now.check_buy_now_page()

@then('we should land to login page')
def step_impl(context):
    '''logic to detect its a valid login page'''
    print("Login page")





