import allure
import data.urls
import data.variables
import locators.dashboard_locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    basic = locators.dashboard_locators.DashboardLocators

    @allure.step('Переход на сайт')
    def go_to_site(self):
        self.get_site(data.urls.SITE)

    @allure.step('Нажатие на кнопку Login')
    def click_button_login(self):
        super().wait_element_clickable(self.basic.login)
        super().click(self.basic.login)

    @allure.step('Ввод имени пользователя')
    def input_name_text(self):
        super().wait_element_located(self.basic.user_name)
        super().input_text(self.basic.user_name, data.variables.NAME)

    @allure.step('Ввод пароля')
    def input_password_text(self):
        super().wait_element_located(self.basic.password)
        super().input_text(self.basic.password, data.variables.PASSWORD)

    @allure.step('Ввод неверного имени пользователя')
    def input_bad_name_text(self):
        super().wait_element_located(self.basic.user_name)
        super().input_text(self.basic.user_name, data.variables.BAD_NAME)

    @allure.step('Ввод неверного пароля')
    def input_bad_password_text(self):
        super().wait_element_located(self.basic.password)
        super().input_text(self.basic.password, data.variables.BAD_PASSWORD)

    @allure.step('Получение текста ошибки invalid_credentials')
    def get_invalid_credentials(self):
        super().wait_element_located(self.basic.invalid_credentials_msg)
        return super().get_text_of_element(self.basic.invalid_credentials_msg)

    @allure.step('Получение текста Login')
    def get_login_text(self):
        super().wait_element_located(self.basic.login_text)
        return super().get_text_of_element(self.basic.login_text)
