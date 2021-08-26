from behave import *
import logging
from modules.login import Login
from modules.constants import Scenarios

# remove added for debug
import time

@given('Is product page has "login as guest" feature')
def step_impl(context):
    # for testing code
    context.web.open(context.url)
    time.sleep(20)
    # set context variables for this specific scenario
    context.found_login_as_guest = True
    login = Login(context)
    # save it in this scenario context to use it in "when" and "then"
    context.login_object = login
    login.find_login_as_guest_feature()

@when('product page support "login as guest" feature')
def step_impl(context):
    if context.found_login_as_guest:
        # skip login scenario
        context.web.skip_scenario(Scenarios.LOGIN)
    else:
        # skip current scenario and proceed to login flow
        context.scenario.skip(reason='Login as Guest not found!! Proceed with login\n')

@then('we should perform "login as guest"')
def step_impl(context):
    context.login_object.click_on_login_as_guest()

@given('Is "login" required')
def step_impl(context):
    # set context variables for this specific scenario
    context.is_login_required = True
    context.some_other_page = False
    login = Login(context)
    # save it in this scenario context to use it in "when" and "then"
    context.login_object = login
    login.check_is_login_required()

@then('perform "login" with credentials')
def step_impl(context):
    if context.is_login_required:
        # Skip all remainig scenarios because we dont support login
        print("Login required to proceed further for this website, we dont support login right now!\n")
        context.web.skip_all_remaining_scenarios()
    elif context.some_other_page:
        # Skip all remainig scenarios because we are on page that was not expected
        print("No Checkout, No Login, Unexpcted page\n")
        context.web.skip_all_remaining_scenarios()
    else:
        print("All good\n")