from controls.button import Button
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("driver")
class AccessDeniedPage:
    def __init__(self):
        self.__back_to_login_page_button = None

    def get_back_to_login_page_button(self):
        self.__back_to_login_page_button = Button(self._driver.find_element(By.XPATH,
                                                                            "//*[text()='back to log in page']"))
        return self.__back_to_login_page_button
