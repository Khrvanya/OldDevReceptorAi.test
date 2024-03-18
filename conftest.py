import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions


@pytest.fixture
def driver(request):
    opts = FirefoxOptions()
    opts.add_argument("--headless")

    driver = webdriver.Firefox(options=opts)
    request.cls.driver = driver

    driver.get("https://dev.receptor.ai/login")

    print("WebDriver instance created successfully")

    driver.implicitly_wait(10)

    yield driver
    driver.quit()
