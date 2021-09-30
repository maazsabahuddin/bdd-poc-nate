# Framework import
from behave import *

# Local import
from modules.confirm_and_pay import ConfirmAndPay


@given('order confirmation page')
def step_impl(context):
    confirm_and_pay = ConfirmAndPay(context)
    confirm_and_pay.find_confirm_and_pay()
    context.current_obj = confirm_and_pay


@when('confirm and pay found and interactable')
def step_impl(context):
    if context.current_obj.is_confirm_and_pay_found:
        pass
    else:
        context.scenario.skip(reason="Order confirmation and pay button not found")


@then('confirm order and pay')
def step_impl(context):
    context.current_obj.hit_confirm_and_pay()
