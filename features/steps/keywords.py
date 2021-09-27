# Framework import
from behave import *

# Local import
from modules.keywords import KeyWords


@given('product page')
def step_impl(context):
    keywords = KeyWords(context)
    keywords.find_keywords()
    context.current_obj = keywords


@when('keywords found')
def step_impl(context):
    if not context.current_obj.is_keywords_found:
        context.scenario.skip(reason="Keywords not found")


@then('skip checkout step 2 and process further')
def step_impl(context):
    context.current_obj.skip_checkout_step_2()