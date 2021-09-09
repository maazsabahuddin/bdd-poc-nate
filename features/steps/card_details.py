# Framework import
from utility.user_personal_info import UserInfo
from behave import *

# Local import
from modules.card_details import CardDetails

@given('order card details page')
def step_impl(context):
    card_details = CardDetails(context)
    card_details.find_card_details_elements()
    context.current_obj = card_details
    
@when('card details found')
def step_impl(context):
    if context.current_obj.is_card_details_found:
        pass
    else:
        context.scenario.skip(reason="Required fields not found")

@then('fill the details and proceed to next step')
def step_impl(context):
    context.current_obj.select_and_populate_card_details(UserInfo.CARD_NUMBER, UserInfo.CARD_HOLDER_NAME, 
        UserInfo.CARD_MONTH_EXPIRY, UserInfo.CARD_YEAR_EXPIRY, UserInfo.CARD_CVV, UserInfo.CARD_EXPIRY)