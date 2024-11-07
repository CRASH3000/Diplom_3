from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls_site_data import UrlsSiteData

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        self.driver.get(UrlsSiteData.LOGIN_URL)

    def open_restore_password_page(self):
        self.driver.get(UrlsSiteData.RESET_PASSWORD_URL)

    def wait_restore_password_page(self):
        self.wait.until(
            EC.url_to_be(UrlsSiteData.RESET_PASSWORD_URL)
        )

    def click_restore_password_button(self):
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.RESTORE_PASSWORD_BUTTON)).click()

    def enter_email(self, email):
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)).send_keys(password)

    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()

    def click_restore_button(self):
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.RESTORE_BUTTON)).click()

    def click_toggle_password_visibility(self):
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.TOGGLE_PASSWORD_VISIBILITY)
        )
        self.driver.find_element(*LoginPageLocators.TOGGLE_PASSWORD_VISIBILITY).click()

    def is_password_field_active(self):
        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        return self.wait.until(lambda driver: "input_status_active" in password_field.get_attribute("class"))