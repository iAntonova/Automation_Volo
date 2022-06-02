from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PythonOrgSearchPage:
    URL = 'https://www.python.org/'
    SEARCH_INPUT = (By.ID, 'id-search-field')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = self.driver.find_element(
            *self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
