from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Локатор для кнопки "Восстановить пароль" на странице авторизации
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")

    # Локатор для поля ввода email на странице восстановления пароля
    EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']")

    # Локатор для поля пароля на странице сброса пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']")

    # Локатор для кнопки "Войти" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")

    # Локатор для кнопки "Восстановить" на странице восстановления пароля
    RESTORE_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Восстановить']")

    # Локатор для значка "Показать/Скрыть пароль" на странице сброса пароля
    TOGGLE_PASSWORD_VISIBILITY = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]")

    PASSWORD_FIELD = (By.CLASS_NAME, "input")

    TOGGLE_PASSWORD_VISIBILITY_BUTTON = (By.CLASS_NAME, "input__icon-action")

