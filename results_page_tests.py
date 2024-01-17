from driver import Driver
from pages.login_page import LoginPage
from pages.access_denied_page import AccessDeniedPage
from pages.dashboard_page import DashboardPage
from pages.results_page import ResultsPage


class TestResultsPage:
    def setup_class(self):
        self.driver = Driver.get_firefox_driver()
        self.login_page = LoginPage()
        self.access_denied_page = AccessDeniedPage()
        self.dashboard_page = DashboardPage()
        self.results_page = ResultsPage()
        self.driver.get("https://dev.receptor.ai/login")
        self.login_page.get_email_field().fill_field("yana.shevchenko@receptor.ai")
        self.login_page.get_password_field().fill_field("HG4dYfgMIrqHZED5")
        self.login_page.get_sign_in_button().click()

    def setup_method(self):
        self.results_page.get_logo_header_button().click()

    def test_radar_chart_window_is_displayed_after_click_on_name(self):
        self.dashboard_page.get_open_button().click()
        self.results_page.get_molecule_name_button().click()
        assert self.results_page.get_radar_chart_button().is_displayed()

    def test_range_slider_is_present(self):
        self.dashboard_page.get_open_button().click()
        self.results_page.get_molecule_name_button().click()
        self.results_page.get_molecule_viewer_button().click()
        assert self.results_page.get_surface_radius_range_slider().is_displayed()

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.quit()
