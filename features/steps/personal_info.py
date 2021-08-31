from behave import *
# Local import
from modules.personal_info import PersonalInfo
from utility.user_personal_info import UserInfo

@given('information required page')
def step_impl(context):
    personal_information = PersonalInfo(context)
    personal_information.find_personal_info_elements()
    context.current_obj = personal_information

@when('personal information is required')
def step_impl(context):
    if context.current_obj.is_required_field_found:
        print("requred field found")
        pass
    else:
        context.scenario.skip(reason='required field not found')

@then('fill the information and proceed to next step')
def step_impl(context):
    if context.current_obj.email is not None:
        email = UserInfo.EMAIL
    else:
        email = None
    if context.current_obj.first_name is not None:
        first_name = UserInfo.FIRST_NAME
    else:
        first_name = None
    if context.current_obj.last_name is not None:
        last_name = UserInfo.LAST_NAME
    else:
        last_name = None
    if context.current_obj.phone is not None:
        phone = UserInfo.PHONE
    else:
        phone = None
    context.current_obj.fill_required_info(email, first_name, last_name, phone)
    if context.current_obj.is_data_populated:
        context.current_obj.hit_to_proceed()