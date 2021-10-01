# Framework Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Local imports
from file import close_file
from modules.logger import logger
from modules.base import Base
from utility import constants
from utility.constants import SkipScenario, Timer, ETC
from app import _result_file


def before_all(context):
    """
    This function run before the whole shooting match
    :param context:
    """
    if not context.config.log_capture:
        context.config.setup_logging()
    logger.info("Logs enabled..")

    # This flag will be used to skip all future scenarios, can be set from anywhere
    context._root[SkipScenario.SKIP_ALL] = False
    # This flag will be used to tell if the whole website flow is failed or passed
    context._root[ETC.IS_CASE_FAILED] = False

    # This dict will be used to skip individual scenarios along the run
    context._root[SkipScenario.SKIP_SCENARIO] = {SkipScenario.SKIP_LOGIN: False, SkipScenario.SKIP_ADD_TO_CART: False}

    # This give the options object of chrome browser
    logger.info("Extending chrome options")
    chrome_options = webdriver.ChromeOptions()

    # This will disable usb driver error log to disable
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    # TODO We can make use of this chrome option below of enable-automation as to hide
    #  "Chrome is being controlled by automated test software" when we run script.

    # This will disable automation extension to bypass bot detection
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # This option disable automation controls to bypass bot detection
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # This context attributes is available throughout all scenarios
    logger.info("Install chrome driver or retrieve from cache.")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # This will maximize the browser window
    logger.info("Maximizing chrome window.")
    browser.maximize_window()

    # This make the browser to wait for given number of seconds to load page

    logger.info(f"Page load timeout set to {Timer.PAGE_LOAD_TIMEOUT} seconds.")
    browser.set_page_load_timeout(Timer.PAGE_LOAD_TIMEOUT)

    logger.info("Setting url and web object.")
    context.url = context.config.userdata[ETC.URL]
    context.name = context.config.userdata.get(ETC.NAME)
    context.log = context.config.userdata.get(ETC.LOG)
    context.color = extract_user_data(context, ETC.COLOR)
    context.size = extract_user_data(context, ETC.SIZE)
    context.BEHAVE_DEBUG_ON_ERROR = context.config.userdata.getbool(ETC.BEHAVE_DEBUG_ON_ERROR)
    web = Base(browser, context)
    context.web = web


def extract_user_data(context, key):
    data = context.config.userdata.get(key)
    data_dict = {}
    if not data:
        return data_dict
    for val in data.split(','):
        value = val.split(':')
        data_dict.update({value[0]: value[1].replace(".", ' ')})
    return data_dict


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
    This function run before a section scenario tagged with name
    :param context:
    :param tag:
    """
    # add condition for tag on scenario and perform the required operation
    if tag == SkipScenario.SKIP_LOGIN:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_LOGIN):
            context.scenario.skip(reason="No need to login, will go with login as guest")
    if tag == SkipScenario.SKIP_ADD_TO_CART:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_ADD_TO_CART):
            context.scenario.skip(reason="Skip add to cart, because we found buy now")
    if tag == SkipScenario.SKIP_PROCEED_CHECKOUT:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_PROCEED_CHECKOUT):
            context.scenario.skip(reason="Skip proceed to checkout, because we ran the buy now button successfully")
    if tag == SkipScenario.SKIP_PERSONAL_INFO:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_PERSONAL_INFO):
            context.scenario\
                .skip(reason="Skip populate personal information, because website did not support guest feature")


def after_step(context, step):
    if context.BEHAVE_DEBUG_ON_ERROR and step.status == constants.ETC.FAILED:
        import ipdb
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.. STEP FAILS..")
        ipdb.post_mortem(step.exc_traceback)


def failed_case(context, scenario, exception_message):
    try:
        logger.info("Skipping all other scenarios.")
        _result_file.write(f"{context.name} - FAILED - {scenario} - {str(exception_message)}\n") \
            if context.log == "True" else None
        close_file(_result_file)
        context._root[ETC.IS_CASE_FAILED] = True
        context.web.skip_all_remaining_scenarios()
    except ValueError as e:
        logger.info(f"CANNOT WRITE TO FILE. FILE ALREADY CLOSED.. Exception - {str(e)}")
