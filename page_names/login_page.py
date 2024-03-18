from controls.button import Button
from selenium.webdriver.common.by import By
from controls.text_box import TextBox
import pytest


@pytest.mark.usefixtures("driver")
class LoginPage:
    def __init__(self):
        self.__sign_in_button = None
        self.__email_field = None
        self.__password_field = None

    def get_sign_in_button(self):
        self.__sign_in_button = Button(self._driver.find_element(By.XPATH, "//*[@value='sign in'] "))
        return self.__sign_in_button

    def get_email_field(self):
        self.__email_field = TextBox(self._driver.find_element(By.ID, "username"))
        return self.__email_field

    def get_password_field(self):
        self.__password_field = TextBox(self._driver.find_element(By.ID, "password"))
        return self.__password_field





