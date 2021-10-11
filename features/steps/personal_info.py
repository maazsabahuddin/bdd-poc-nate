# Framework imports
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
    if not context.current_obj.is_required_field_found:
        context.scenario.skip(reason='cannot find required fields')


@then('fill the information and proceed to next step')
def step_impl(context):
    email, phone, first_name, last_name = None, None, None, None

    if context.current_obj.email:
        email = UserInfo.EMAIL
    if context.current_obj.first_name:
        first_name = UserInfo.FIRST_NAME
    if context.current_obj.last_name:
        last_name = UserInfo.LAST_NAME
    if context.current_obj.phone:
        phone = UserInfo.PHONE

    context.current_obj.fill_required_info(email, first_name, last_name, phone)
    if context.current_obj.is_data_populated:
        context.current_obj.hit_to_proceed()
