from controls.button import Button
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("driver")
class Header:
    def __init__(self):
        self.__man_icon = None
        self.__sign_out_button = None

    def get_man_icon(self):
        self.__man_icon = Button(self._driver.find_element(By.XPATH,
                                                           "//*[@class='nav-item dropdown receptor-dropdown']"))
        return self.__man_icon

    def get_sign_out_button(self):
        self.__sign_out_button = Button(self._driver.find_element(By.XPATH, "//*[@href='/logout']"))
        return self.__sign_out_button

