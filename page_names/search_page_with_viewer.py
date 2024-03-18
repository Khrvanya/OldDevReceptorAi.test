from controls.button import Button
from selenium.webdriver.common.by import By
from controls.label import Label
import pytest


@pytest.mark.usefixtures("driver")
class SearchPageWithViewer:
    def __init__(self):
        self.__cartoon_representation_label = None
        self.__line_representation_label = None
        self.__add_custom_pocket_button = None
        self.__pocket_center_x_range_slider = None
        self.__preview_pocket_button = None
        self.__confirm_and_create_pocket_button = None
        self.__molecule_viewer = None

    def get_cartoon_representation_label(self):
        self.__cartoon_representation_label = Label(self._driver.find_element(By.ID, "Viz-Settings-Col2"))
        return self.__cartoon_representation_label

    def get_line_representation_label(self):
        self.__line_representation_label = Label(self._driver.find_element(By.ID, "Viz-Settings-Col1"))
        return self.__line_representation_label

    def get_add_custom_pocket_button(self):
        self.__add_custom_pocket_button = Button(self._driver.find_element(By.ID, "pills-add-custom-pocket-tab"))
        return self.__add_custom_pocket_button

    def get_pocket_center_x_range_slider(self):
        self.__pocket_center_x_range_slider = Label(self._driver.find_element(By.ID, "Pocket-X-Coord"))
        return self.__pocket_center_x_range_slider

    def get_preview_pocket_button(self):
        self.__preview_pocket_button = Button(self._driver.find_element(By.ID, "pills-preview-pocket-tab"))
        return self.__preview_pocket_button

    def get_confirm_and_create_pocket_button(self):
        self.__confirm_and_create_pocket_button = Button(self._driver.find_element(By.ID,
                                                                                   "pills - confirm - pocket - tab"))
        return self.__confirm_and_create_pocket_button

    def get_molecule_viewer(self):
        self.__molecule_viewer = Label(self._driver.find_element(By.ID, "Results-Mol-Viewer"))
        return self.__molecule_viewer

