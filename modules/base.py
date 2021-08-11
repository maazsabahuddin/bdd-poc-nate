from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    
    timeout = 10

    def __init__(self, web_driver):
        self.web_driver_wait = WebDriverWait(web_driver, self.timeout)
        self.web_driver = web_driver

    def open(self, url):
        self.web_driver.get(url)
    
    def close_driver(self):
        self.web_driver.quit()

    def find_by_xpath(self, xpath):
        return self.web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def finds_by_xpath(self, xpath):
        return self.web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))