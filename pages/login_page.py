import allure
import data.urls
import data.variables
import locators.dashboard_locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    basic = locators.dashboard_locators.DashboardLocators

    @allure.step('Переход на сайт')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Нажатие на кнопку Login')
    def click_button_login(self):
        super().wait_element_clickable(self.basic.login)
        super().click(self.basic.login)

    @allure.step('Ввод имени пользователя')
    def input_name_text(self):
        super().wait_element_located(self.basic.user_name)
        super().input_text(self.basic.user_name, data.variables.name)

    @allure.step('Ввод пароля')
    def input_password_text(self):
        super().wait_element_located(self.basic.password)
        super().input_text(self.basic.password, data.variables.password)

    @allure.step('Ввод неверного имени пользователя')
    def input_bad_name_text(self):
        super().wait_element_located(self.basic.user_name)
        super().input_text(self.basic.user_name, data.variables.bad_name)

    @allure.step('Ввод неверного пароля')
    def input_bad_password_text(self):
        super().wait_element_located(self.basic.password)
        super().input_text(self.basic.password, data.variables.bad_password)

    @allure.step('Получение текста Dashboard')
    def get_dashboard_title(self):
        super().wait_element_located(self.basic.dashboard_text)
        return super().get_text_of_element(self.basic.dashboard_text)

    @allure.step('Получение текста ошибки invalid_credentials')
    def get_invalid_credentials(self):
        super().wait_element_located(self.basic.invalid_credentials_msg)
        return super().get_text_of_element(self.basic.invalid_credentials_msg)
