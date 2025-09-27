import allure
import locators.dashboard_locators
from pages.login_page import LoginPage


class DashboardPage(LoginPage):
    basic = locators.dashboard_locators.DashboardLocators

    @allure.step('Получение текста Dashboard')
    def get_dashboard_title(self):
        super().wait_element_located(self.basic.dashboard_text)
        return super().get_text_of_element(self.basic.dashboard_text)

    @allure.step('Нажать на свойства профиля')
    def click_profile_properties(self):
        super().wait_element_clickable(self.basic.profile_properties)
        super().click(self.basic.profile_properties)

    @allure.step('Нажать на кнопку logout')
    def click_logout(self):
        super().wait_element_clickable(self.basic.logout)
        super().click(self.basic.logout)
