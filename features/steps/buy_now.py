from behave import *
from modules.buy_now import BuyNow
from modules.constants import SkipScenario

@given('url of product page')
def step_impl(context):
    # create a object
    buy_now = BuyNow(context)
    buy_now.check_buy_now_page()
    context.current_obj = buy_now

@when('buy now found')
def step_impl(context):
    if (context.current_obj.is_buy_now_found):
        context.current_obj.skip_non_required_scenarios()
    else:
        context.scenario.skip(reason='Cannot find buy now button, now finding add to cart button')

@then('click on buy now and proceed to next step')
def step_impl(context):
    pass