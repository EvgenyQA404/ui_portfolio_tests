import allure
from pages.login_page import LoginPage
import data.variables
import data.urls


@allure.parent_suite("Автоматизация UI")
@allure.suite("Примеры тестов UI")
@allure.sub_suite("Основные проверки")
class TestBasicFunctionality:
    @allure.description(
        'После аутентификации поиск текста "Dashboard" в личном кабинете')
    @allure.title('Успешный логин')
    def test_success_login(self, driver):
        page = LoginPage(driver)
        page.go_to_site()
        page.input_name_text()
        page.input_password_text()
        page.click_button_login()
        expected = page.get_dashboard_title()
        assert data.variables.dashboard_text == expected

    @allure.description(
        'После ошибки аутентификации поиск текста "Invalid credentials" на странице логина')
    @allure.title('Неуспешный логин')
    def test_failure_login(self, driver):
        page = LoginPage(driver)
        page.go_to_site()
        page.input_bad_name_text()
        page.input_bad_password_text()
        page.click_button_login()
        expected = page.get_invalid_credentials()
        assert data.variables.invalid_credentials_text == expected
