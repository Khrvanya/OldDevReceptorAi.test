from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:
    driver = None

    # @staticmethod
    def get_firefox_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = webdriver.Firefox()
            Driver.driver.implicitly_wait(10)
            return Driver.driver
        else:
            return Driver.driver

