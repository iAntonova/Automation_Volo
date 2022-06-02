# from selenium import webdriver
from Pages.search import PythonOrgSearchPage
from Pages.result import PythonOrgResultPage
from Lib import Helper, logging


driver = None

# Activate Chrome browser
driver = Helper().driver()
logging.info(f"Testing starts: {driver} initialized")

# Set up test case data
PHRASE = 'python'


# Search for the phrase
search_page = PythonOrgSearchPage(driver)
search_page.load()
search_page.search(PHRASE)

# Verify that results appear
result_page = PythonOrgResultPage(driver)
assert result_page.link_li_count() > 0
logging.info(f"Page displayed: {result_page.link_li_count()} result(s)")
assert result_page.search_input_value() == PHRASE
logging.info("Search word match: true")


# Close browser
Helper().close_driver(driver)
logging.info("Browser closed. Test passed.")
