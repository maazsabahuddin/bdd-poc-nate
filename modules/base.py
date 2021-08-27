# Framework imports
from logging import exception
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
# Local imports
from utility.constants import SkipScenario

class Base:
    
    timeout = 10
    process_pause_time = 5

    def __init__(self, web_driver, context):
        self.web_driver_wait = WebDriverWait(web_driver, self.timeout)
        self.web_driver = web_driver
        self.context = context

    def open(self, url):
        self.web_driver.get(url)
    
    def close_driver(self):
        self.web_driver.quit()
    
    def skip_all_remaining_scenarios(self):
        self.context._root[SkipScenario.SKIP_ALL] = True
    
    def skip_scenario(self, scenario_name):
        self.context._root[SkipScenario.SKIP_SCENARIO].update({scenario_name: True})

    def find_by_xpath_wait(self, xpath):
        try:
            return self.web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except exceptions.TimeoutException:
            return None

    def finds_by_xpath_wait(self, xpath):
        try:
            return self.web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        except exceptions.TimeoutException:
            return []

    def get_current_url(self):
        return self.web_driver.current_url

    def find_cross_by_css_selector_wait(self, xpath):
        return self.web_driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, xpath)))

    def find_by_xpath(self, xpath):
        return self.web_driver.find_element_by_xpath(xpath)
    
    def find_parent_element_from_child(self, child_element):
        parent_elements_list = ["button", "a"]
        try:
            current_found_element = child_element
            for x in range(2):
                parent_element = current_found_element.find_element_by_xpath("..")
                parent_element_name = parent_element.tag_name
                if (parent_element_name in parent_elements_list):
                    return parent_element
                else:
                    current_found_element = parent_element
            return None
        except exceptions.NoSuchElementException:
            return None
