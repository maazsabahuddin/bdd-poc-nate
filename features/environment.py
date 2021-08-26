import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from modules.base import Base
from modules.constants import SkipScenario

'''
This funtion run before the whole shooting match
'''
def before_all(context):
    # This flag will be used to skip all future scenarios, can be set from anywhere
    context._root[SkipScenario.SKIP_ALL] = False
    # This dict will be used to skip indiviaudal scenarios along the run
    context._root[SkipScenario.SKIP_SCENARIO] = {SkipScenario.SKIP_LOGIN: False, SkipScenario.SKIP_ADD_TO_CART: False}
    # This give the options object of chrome browser
    options = webdriver.ChromeOptions()
    # This will disable usb driver error log to disable
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # This context attributes is available throughout all scenarios
    browser = webdriver.Chrome(ChromeDriverManager().install(), options= options)
    # This will maximize the broswer window
    browser.maximize_window()
    context.url = context.config.userdata['url']
    web = Base(browser, context)
    context.web = web

'''
This funtion run after the whole shooting match
'''	
def after_all(context):
	context.web.close_driver()

'''
This funtion run before each scenario is run
'''	
def before_scenario(context, scenario):
    if context._root.get(SkipScenario.SKIP_ALL, True):
        scenario.skip(reason='Not able to proceed!')


'''
This funtion run before a section scenario tagged with name
'''
def before_tag(context, tag):
    # add condition for tag on sceanrio and perform the required operation
    if tag == SkipScenario.SKIP_LOGIN:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_LOGIN):
            context.scenario.skip(reason="No need to login, will go with login as guest")
    if tag == SkipScenario.SKIP_ADD_TO_CART:
        if context._root.get(SkipScenario.SKIP_SCENARIO).get(SkipScenario.SKIP_ADD_TO_CART):
            context.scenario.skip(reason="Skip add to cart, beacuse we found buy now")



