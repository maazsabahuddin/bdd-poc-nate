# Framework imports
from behave import *

# Local imports
from modules.buy_now import BuyNow
from modules.logger import logger


@given('url of product page')
def step_impl(context):
    """
    Check and verify if it is a buy now page or not
    :param context:
    """
    buy_now = BuyNow(context)
    buy_now.check_buy_now_page()


@then('we should land to login page')
def step_impl(context):
    """ logic to detect its a valid login page """
    logger.info("Login page")
