# from page_names.login_page import LoginPage
# from page_names.access_denied_page import AccessDeniedPage
# from page_names.dashboard_page import DashboardPage
# from page_names.results_page import ResultsPage
# from page_names.header import Header
# import pytest
#
#
# @pytest.mark.usefixtures("driver")
# class TestResultsPage:
#     def setup_class(self, driver):
#         self.login_page = LoginPage()
#         self.access_denied_page = AccessDeniedPage()
#         self.dashboard_page = DashboardPage()
#         self.results_page = ResultsPage()
#         self.header = Header()
#         self.driver.get("https://dev.receptor.ai/login")
#         self.login_page.get_email_field().fill_field("yana.shevchenko@receptor.ai")
#         self.login_page.get_password_field().fill_field("HG4dYfgMIrqHZED5")
#         self.login_page.get_sign_in_button().click()
#
#     def setup_method(self, driver):
#         self.results_page.get_logo_header_button().click()
#
#     def test_radar_chart_window_is_displayed_after_click_on_name(self, driver):
#         self.dashboard_page.get_open_button().click()
#         self.results_page.get_molecule_name_button().click()
#         assert self.results_page.get_radar_chart_button().is_displayed()
#
#     def test_range_slider_is_present(self, driver):
#         self.dashboard_page.get_open_button().click()
#         self.results_page.get_molecule_name_button().click()
#         self.results_page.get_molecule_viewer_button().click()
#         assert self.results_page.get_surface_radius_range_slider().is_displayed()
#         self.results_page.get_x_out_button().click()
#         self.results_page.get_logo_header_button().click()
#
#     def teardown_method(self, driver):
#         pass
#
#
#
#
#
#
