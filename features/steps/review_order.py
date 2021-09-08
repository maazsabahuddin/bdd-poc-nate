# Framework imports
from behave import *

# Local imports
from modules.review_order import ReviewOrder


@given('order page')
def step_impl(context):
    review_order = ReviewOrder(context)
    review_order.find_review_order()
    context.current_obj = review_order


@when('review order button found')
def step_impl(context):
    if context.current_obj.is_review_order_found:
        pass
    else:
        context.scenario.skip(reason="Review order button not found, it means no need to review order")


@then('review order and proceed to next step')
def step_impl(context):
    context.current_obj.hit_review_order()
