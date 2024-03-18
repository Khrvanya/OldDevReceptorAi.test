from controls.button import Button
from selenium.webdriver.common.by import By
from controls.text_box import TextBox
import pytest


@pytest.mark.usefixtures("driver")
class SearchPageTargetSelection:
    def __init__(self):
        self.__uniprot_id_field = None
        self.__a0avt1_button_in_search_window = None
        self.__password_field = None
        self.__new_project_button_header = None
        self.__new_project_name_field = None
        self.__new_project_create_button = None

    def get_uniprot_id_field(self):
        self.__uniprot_id_field = TextBox(self._driver.find_element(By.ID, "Target-Query"))
        return self.__uniprot_id_field

    def get_a0avt1_button_in_search_window(self):
        self.__a0avt1_button_in_search_window = Button(self._driver.find_element(By.XPATH, "//*[text()='A0AVT1']"))
        return self.__a0avt1_button_in_search_window

