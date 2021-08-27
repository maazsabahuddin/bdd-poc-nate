# Framework Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Local Imports
from modules.base import Base
from modules.constants import SkipScenario


def before_all(context):
    """
    This function run before the whole shooting match
    :param context:
    """
    # This flag will be used to skip all future scenarios, can be set from anywhere
    context.config.setup_logging()
    context._root[SkipScenario.SKIP_ALL] = False
    # This dict will be used to skip indiviaudal scenarios along the run
    context._root[SkipScenario.SKIP_SCENARIO] = {SkipScenario.SKIP_LOGIN: False, SkipScenario.SKIP_ADD_TO_CART: False}
    # This context attributes is available throughout all scenarios
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # This will maximize the broswer window
    browser.maximize_window()
    context.url = context.config.userdata['url']
    web = Base(browser, context)
    context.web = web


def after_all(context):
    """
    This function run after the whole shooting match
    :param context:
    """
    context.web.close_driver()


def before_scenario(context, scenario):
    """
    This function run before each scenario is run
    :param context:
    :param scenario:
    """
    if context._root.get(SkipScenario.SKIP_ALL, True):
        scenario.skip(reason='Not able to proceed!')


def before_tag(context, tag):
    """
    This funtion run before a section scenario tagged with name
    :param context:
    :param tag:
    """
    # add condition for tag on sceanrio and perform the required operation
    if tag == SkipScenario.SKIP_LOGIN:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_LOGIN):
            context.scenario.skip(reason="No need to login, will go with login as guest")
    if tag == SkipScenario.SKIP_ADD_TO_CART:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_ADD_TO_CART):
            context.scenario.skip(reason="Skip add to cart, beacuse we found buy now")
