from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import FirefoxOptions


class Driver:
    driver = None
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(options=opts)

    @staticmethod
    def get_firefox_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = Driver.browser
            Driver.driver.implicitly_wait(10)
            return Driver.driver
        else:
            return Driver.driver

