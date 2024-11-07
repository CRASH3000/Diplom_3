from selenium.webdriver.remote.webdriver import WebDriver
from locators.profile_page_locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go_to_order_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ORDER_HISTORY_BUTTON)
        ).click()

    def get_last_order_in_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.ORDER_HISTORY_LIST)
        )
        last_order_number_element = self.driver.find_element(*ProfilePageLocators.LAST_ORDER_NUMBER)
        last_order_number = last_order_number_element.text

        return last_order_number

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()

