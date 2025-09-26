from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators


class DashboardLocators(LoginLocators):
    # текст Dashboard в личном кабинете
    dashboard_text = (By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module') and normalize-space("
                                ")='Dashboard']")
