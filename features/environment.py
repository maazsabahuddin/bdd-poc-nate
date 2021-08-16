import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from modules.base import Base

'''
This funtion run before the whole shooting match
'''
def before_all(context):
    # This flag will be used to skip all future scenarios, can be set from anywhere
    context._root['skip_all'] = False
    # This dict will be used to skip indiviaudal scenarios along the run
    context._root["skip_scenario"] = {"skip_login": False}
    # This context attributes is available throughout all scenarios
    browser = webdriver.Chrome(ChromeDriverManager().install())
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
    if context._root.get('skip_all', True):
        scenario.skip(reason='Not able to proceed!')


'''
This funtion run before a section scenario tagged with name
'''
def before_tag(context, tag):
    # add condition for tag on sceanrio and perform the required operation
    if tag == "skip_login":
        if context._root.get('skip_scenario').get('skip_login'):
            context.scenario.skip(reason="Skip login, will go with login as guest")



