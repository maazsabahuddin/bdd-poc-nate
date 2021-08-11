from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from modules.base import Base

def before_all(context):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    context.url = context.config.userdata['url']
    web = Base(browser)
    context.web = web

	
def after_all(context):
	context.web.close_driver()