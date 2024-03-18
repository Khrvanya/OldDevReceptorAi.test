from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import FirefoxOptions


# class Driver:
#     driver = None
#     opts = FirefoxOptions()
#     opts.add_argument("--headless")
#     browser = webdriver.Firefox(options=opts)
#
#     @staticmethod
#     def get_firefox_driver() -> WebDriver:
#         if Driver.driver is None:
#             Driver.driver = Driver.browser
#             Driver.driver.implicitly_wait(10)
#             return Driver.driver
#         else:
#             return Driver.driver

import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions


@pytest.fixture(scope="session")
def driver():
    # Create a FirefoxOptions instance
    opts = FirefoxOptions()
    opts.add_argument("--headless")

    # Create a WebDriver instance
    driver = webdriver.Firefox(options=opts)

    # Set implicit wait time
    driver.implicitly_wait(10)

    # Return the WebDriver instance
    yield driver

    # Teardown: quit the WebDriver instance after all tests in the session
    driver.quit()