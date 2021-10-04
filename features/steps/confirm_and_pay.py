# Framework import
from behave import *

# Local import
from features.environment import failed_case
from file import close_file
from modules.confirm_and_pay import ConfirmAndPay
from utility.constants import ETC
from app import _result_file


@given('order confirmation page')
def step_impl(context):
    confirm_and_pay = ConfirmAndPay(context)
    confirm_and_pay.find_confirm_and_pay()
    context.current_obj = confirm_and_pay


@when('confirm and pay found and interactable')
def step_impl(context):
    if not context.current_obj.is_confirm_and_pay_found:
        context.scenario.skip(reason="Order confirmation and pay button not found")
        failed_case(context=context,
                    scenario="Confirm And Pay",
                    exception_message="Order confirmation and pay button not found")


@then('confirm order and pay')
def step_impl(context):
    context.current_obj.hit_confirm_and_pay()
    if not context._root[ETC.IS_CASE_FAILED]:
        _result_file.write(f"{context.name} - PASSED\n") if context.log == "True" else None
        close_file(_result_file)
