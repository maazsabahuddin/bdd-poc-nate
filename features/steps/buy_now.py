# Framework imports
from behave import *

# Local imports
from modules import logger
from modules.buy_now import BuyNow


@given('url of product page')
def step_impl(context):
    """
    Check and verify if it is a buy now page or not
    :param context:
    """
    buy_now = BuyNow(context)
    buy_now.check_buy_now_page()
    context.current_obj = buy_now


@then('we should land to login page')
def step_impl(context):
    """ logic to detect its a valid login page """
    # logger.info("Login page")
    pass


@when('buy now found')
def step_impl(context):
    if context.current_obj.is_buy_now_found:
        context.current_obj.skip_non_required_scenarios()
    else:
        context.scenario.skip(reason='Cannot find buy now button, now finding add to cart button')


@then('click on buy now and proceed to next step')
def step_impl(context):
    """logic to detect its a valid login page"""
    if context.buy_now_found:
        print("Login page")
    else:
        print("buy now not found move to next senario to find add to ... button")

    context.current_obj.hit_buy_now_element()
