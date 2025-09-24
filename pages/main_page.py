import allure
import data.urls
import data.variables
import locators.main_locators
from pages.basic_page import BasePage


class BasicFunctionalityPage(BasePage):
    basic = locators.main_locators.MainLocators

    @allure.step('Переход на тестовый сайт')
    def go_to_site(self):
        super().get_site(data.urls.site)

    @allure.step('Нажатие на кнопку Login')
    def click_button_login(self):
        super().wait_element_clickable(self.basic.login)
        super().click_on_section(self.basic.login)

    @allure.step('Ввод имени пользователя')
    def input_name_text(self):
        super().input_text(self.basic.user_name, data.variables.name)

    @allure.step('Ввод пароля')
    def input_password_text(self):
        super().input_text(self.basic.password, data.variables.password)

    @allure.step('Получение текста Dashboard')
    def get_text_of_element(self):
        return super().get_text_of_element(self.basic.dashboard_text)
