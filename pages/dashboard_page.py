from controls.button import Button
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from controls.label import Label
from controls.text_box import TextBox


class DashboardPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__page_name_header = None
        self.__open_button = None
        self.__password_field = None
        self.__new_project_button_header = None
        self.__new_project_name_field = None
        self.__new_project_create_button = None

    def get_page_name_header(self):
        self.__page_name_header = Label(self._driver.find_element(By.XPATH, "//*[@class='m-0 mb-2 content-header-h1']"))
        return self.__page_name_header

    def get_open_button(self):
        self.__open_button = Button(self._driver.find_element(By.XPATH, "//a[@href='/project/results/85']"))
        return self.__open_button

    def get_new_project_button_header(self):
        self.__new_project_button_header = Button(self._driver.find_element(By.ID, "New-Project"))
        return self.__new_project_button_header

    def get_new_project_name_field(self):
        self.__new_project_name_field = TextBox(self._driver.find_element(By.ID, "New-Project-Name"))
        return self.__new_project_name_field

    def get_new_project_create_button(self):
        self.__new_project_create_button = Button(self._driver.find_element(By.ID, "Control-Sidebar-Submit-Btn"))
        return self.__new_project_create_button







