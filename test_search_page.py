# from driver import Driver
# from pages.login_page import LoginPage
# from pages.access_denied_page import AccessDeniedPage
# from pages.dashboard_page import DashboardPage
# from pages.results_page import ResultsPage
# from pages.search_page_with_viewer import SearchPageWithViewer
# from pages.search_page_target_selection import SearchPageTargetSelection
#
#
# class TestSearchPage:
#     def setup_class(self):
#         self.driver = Driver.get_firefox_driver()
#         self.login_page = LoginPage()
#         self.access_denied_page = AccessDeniedPage()
#         self.dashboard_page = DashboardPage()
#         self.results_page = ResultsPage()
#         self.search_page_with_viewer = SearchPageWithViewer()
#         self.search_page_target_selection = SearchPageTargetSelection()
#         self.driver.get("https://dev.receptor.ai/login")
#         self.login_page.get_email_field().fill_field("yana.shevchenko@receptor.ai")
#         self.login_page.get_password_field().fill_field("HG4dYfgMIrqHZED5")
#         self.login_page.get_sign_in_button().click()
#         self.dashboard_page.get_new_project_button_header().click()
#         self.dashboard_page.get_new_project_name_field().fill_field("test")
#         self.dashboard_page.get_new_project_create_button().click()
#
#     def setup_method(self):
#         pass
#
#     def test_choose_uniprot_id_from_the_list(self):
#         self.search_page_target_selection.get_uniprot_id_field().fill_field("G ").click_on_enter(Keys.ENTER)
#         self.search_page_target_selection.get_a0avt1_button_in_search_window().click()
#         self.search_page_with_viewer.get_molecule_viewer().is_displayed()
#
#     def teardown_method(self):
#         pass
#
#     def teardown_class(self):
#         self.driver.quit()
