from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators


class DashboardLocators(LoginLocators):
    # текст Dashboard в личном кабинете
    dashboard_text = (By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module') and normalize-space("
                                ")='Dashboard']")
    # свойства профиля в личном кабинете
    profile_properties = (By.XPATH, "//p[contains(@class,'oxd-userdropdown-name')]")
    # выход из личного кабинет
    logout = (By.XPATH, "//a[@href='/web/index.php/auth/logout' and contains(@class,'oxd-userdropdown-link') and "
                        "normalize-space()='Logout']")
