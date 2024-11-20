import allure
from locators.login_page_locators import LoginPageLocators
from data.urls_site_data import UrlsSiteData
from page_objects.base_page import BasePage

class LoginPage (BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.open_url(UrlsSiteData.LOGIN_URL)

    @allure.step("Открытие страницы восстановления пароля")
    def open_restore_password_page(self):
        self.open_url(UrlsSiteData.RESET_PASSWORD_URL)

    @allure.step("Ожидание загрузки страницы восстановления пароля")
    def wait_restore_password_page(self):
        self.wait_for_url(UrlsSiteData.RESET_PASSWORD_URL)

    @allure.step("Клик по кнопке восстановления пароля")
    def click_restore_password_button(self):
        self.click(LoginPageLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Ввод email")
    def enter_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click(LoginPageLocators.RESTORE_BUTTON)

    @allure.step("Клик по кнопке показа/скрытия пароля")
    def click_toggle_password_visibility(self):
        self.click(LoginPageLocators.TOGGLE_PASSWORD_VISIBILITY)

    @allure.step("Проверка активации поля пароля")
    def is_password_field_active(self):
        return self.is_element_active(LoginPageLocators.PASSWORD_FIELD)