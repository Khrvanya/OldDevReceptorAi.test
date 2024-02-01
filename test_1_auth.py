from driver import Driver
from pages.login_page import LoginPage
from pages.access_denied_page import AccessDeniedPage
from pages.dashboard_page import DashboardPage
from pages.header import Header
from pages.results_page import ResultsPage


class TestLogin:
    def setup_class(self):
        self.driver = Driver.get_firefox_driver()
        self.login_page = LoginPage()
        self.access_denied_page = AccessDeniedPage()
        self.dashboard_page = DashboardPage()
        self.results_page = ResultsPage()
        self.header = Header()

    def setup_method(self):
        self.driver.get("https://dev.receptor.ai/login")

    def test_successful_login(self):
        self.login_page.get_email_field().fill_field("yana.shevchenko@receptor.ai")
        self.login_page.get_password_field().fill_field("HG4dYfgMIrqHZED5")
        self.login_page.get_sign_in_button().click()
        assert self.dashboard_page.get_page_name_header().is_displayed()

    def test_wrong_email(self):
        self.login_page.get_email_field().fill_field("yana@receptor.ai")
        self.login_page.get_password_field().fill_field("HG4dYfgMIrqHZED5")
        self.login_page.get_sign_in_button().click()
        assert self.access_denied_page.get_back_to_login_page_button().is_displayed()

    def test_wrong_password(self):
        self.login_page.get_email_field().fill_field("yana.shevchenko@receptor.ai")
        self.login_page.get_password_field().fill_field("qwerty")
        self.login_page.get_sign_in_button().click()
        assert self.access_denied_page.get_back_to_login_page_button().is_displayed()

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.quit()
        self.driver = None


