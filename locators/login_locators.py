from selenium.webdriver.common.by import By


class LoginLocators:
    # поле имя пользователя
    user_name = (By.XPATH, "//input[@name='username']")
    # поле пароль
    password = (By.XPATH, "//input[@name='password']")
    # кнопка логин
    login = (By.XPATH, "//button[@type='submit' and normalize-space(.)='Login']")
    # текст с ошибкой в логине или пароле
    invalid_credentials_msg = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    # текст логина на главной страницы
    login_text = (By.XPATH, "//h5[contains(@class,'orangehrm-login-title') and normalize-space()='Login']")
