from controls.button import Button
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccessDeniedPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__back_to_login_page_button = None

    def get_back_to_login_page_button(self):
        self.__back_to_login_page_button = Button(self._driver.find_element(By.XPATH,
                                                                            "//*[text()='back to log in page']"))
        return self.__back_to_login_page_button
