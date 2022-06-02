from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgResultPage:

    LINK_LIS = (By.CSS_SELECTOR, '#content > div > section > form > ul > li')
    SEARCH_INPUT = (By.XPATH, '//*[@id="content"]/div/section/form/p/input[1]')

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//*[@id='content']/div/section/form/ul//*[contains(text(), \
            '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, driver):
        self.driver = driver

    def link_li_count(self):
        link_lis = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.LINK_LIS)
        )
        return len(link_lis)

    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
