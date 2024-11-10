from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls_site_data import UrlsSiteData
from page_objects.base_page import BasePage

class LoginPage (BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(UrlsSiteData.LOGIN_URL)

    def open_restore_password_page(self):
        self.open_url(UrlsSiteData.RESET_PASSWORD_URL)

    def wait_restore_password_page(self):
        self.wait_for_url(UrlsSiteData.RESET_PASSWORD_URL)

    def click_restore_password_button(self):
        self.click(LoginPageLocators.RESTORE_PASSWORD_BUTTON)

    def enter_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def click_restore_button(self):
        self.click(LoginPageLocators.RESTORE_BUTTON)

    def click_toggle_password_visibility(self):
        self.click(LoginPageLocators.TOGGLE_PASSWORD_VISIBILITY)

    def is_password_field_active(self):
        return self.is_element_active(LoginPageLocators.PASSWORD_FIELD)