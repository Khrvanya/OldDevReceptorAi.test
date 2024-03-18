from page_names.login_page import LoginPage
from page_names.access_denied_page import AccessDeniedPage
from page_names.dashboard_page import DashboardPage
from page_names.header import Header
from page_names.results_page import ResultsPage
import pytest


@pytest.mark.usefixtures("driver")
class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage()
        cls.access_denied_page = AccessDeniedPage()
        cls.dashboard_page = DashboardPage()
        cls.results_page = ResultsPage()
        cls.header = Header()

    @classmethod
    def setup_method(cls):
        pass

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





