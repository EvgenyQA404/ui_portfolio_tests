from selenium.webdriver.common.by import By


class MainLocators:
    # поле имя пользователя
    user_name = [By.XPATH, "//input[@name='username']"]
    # поле пароль
    password = [By.XPATH, "//input[@name='password']"]
    # кнопка логин
    login = [By.XPATH, "//button[@type='submit' and normalize-space(.)='Login']"]
    # текст Dashboard в личном кабинете
    dashboard_text = [By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module') and normalize-space("
                                  ")='Dashboard']"]

