import allure
from locators.profile_page_locators import ProfilePageLocators
from page_objects.base_page import BasePage

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход в историю заказов в профиле")
    def go_to_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Получение последнего заказа в истории заказов")
    def get_last_order_in_history(self):
        self.wait_until_visible(ProfilePageLocators.ORDER_HISTORY_LIST)
        return self.get_text(ProfilePageLocators.LAST_ORDER_NUMBER)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

