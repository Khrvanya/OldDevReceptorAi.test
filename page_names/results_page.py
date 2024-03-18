from controls.button import Button
from selenium.webdriver.common.by import By
from controls.label import Label
import pytest


@pytest.mark.usefixtures("driver")
class ResultsPage:
    def __init__(self):
        self.__molecule_name_button = None
        self.__logo_header_button = None
        self.__radar_chart_button = None
        self.__surface_radius_range_slider = None
        self.__molecule_viewer_button = None
        self.__x_out_button = None

    def get_molecule_name_button(self):
        self.__molecule_name_button = Button(self._driver.find_element(By.XPATH, "//*[text()='R02238694']"))
        return self.__molecule_name_button

    def get_logo_header_button(self):
        self.__logo_header_button = Button(self._driver.find_element(By.XPATH, "//*[@class='navbar-brand']"))
        return self.__logo_header_button

    def get_radar_chart_button(self):
        self.__radar_chart_button = Button(self._driver.find_element(By.ID, "pills-radar-tab"))
        return self.__radar_chart_button

    def get_molecule_viewer_button(self):
        self.__molecule_viewer_button = Button(self._driver.find_element(By.ID, "pills-molecule-view-tab"))
        return self.__molecule_viewer_button

    def get_surface_radius_range_slider(self):
        self.__surface_radius_range_slider = Label(self._driver.find_element(By.ID, "Pocket-Radius-Clipping"))
        return self.__surface_radius_range_slider

    def get_x_out_button(self):
        self.__x_out_button = Button(self._driver.find_element(By.XPATH,
                                                               "//*[@class='close-receptor-control-sidebar']"))
        return self.__x_out_button
