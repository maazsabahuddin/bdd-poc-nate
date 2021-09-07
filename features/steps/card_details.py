# Framework import
from behave import *

# Local import
from modules.card_details import CardDetails

@given('order card details page')
def step_impl(context):
    card_details = CardDetails(context)
    context.current_obj = card_details
    
@when('card details found')
def step_impl(context):
    pass

@then('fill the details and proceed to next step')
def step_impl(context):
    pass