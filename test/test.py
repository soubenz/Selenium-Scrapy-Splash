from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    # initialize options
    options = webdriver.ChromeOptions()
    # pass in headless argument to options
    options.add_argument('--headless')
    # initialize driver
    driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    return driver

    




