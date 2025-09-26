import allure
import time

from pages.login_page import LoginPage
import data.variables
import data.urls


class TestBasicFunctionality:

    @allure.title('Успешный логин')
    def test_success_login(self, driver):
        page = LoginPage(driver)
        page.go_to_site()
        page.input_name_text()
        page.input_password_text()
        page.click_button_login()
        expected = page.get_dashboard_title()
        assert data.variables.dashboard_text == expected

    @allure.title('Неуспешный логин')
    def test_failure_login(self, driver):
        page = LoginPage(driver)
        page.go_to_site()
        page.input_bad_name_text()
        page.input_bad_password_text()
        page.click_button_login()
        time.sleep(3)
        expected = page.get_invalid_credentials()
        assert data.variables.invalid_credentials_text == expected
