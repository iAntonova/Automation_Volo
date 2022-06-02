from selenium import webdriver
import logging


# Logging config
logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(filename)s ' '%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='w+')


class Helper:

    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

    def close_driver(self, driver):
        if driver:
            driver.quit()
