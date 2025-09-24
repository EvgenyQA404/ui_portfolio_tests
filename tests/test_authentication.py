import allure
from pages.main_page import BasicFunctionalityPage
import data.variables
import data.urls


class TestBasicFunctionality:

    @allure.title('Успешный логин')
    def test_success_login(self, driver):
        page = BasicFunctionalityPage(driver)
        page.go_to_site()
        page.input_name_text()
        page.input_password_text()
        page.click_button_login()
        excepted = page.get_text_of_element()
        assert data.variables.dashboard_text == excepted
