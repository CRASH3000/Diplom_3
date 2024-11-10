import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from locators.order_feed_locators import OrderFeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls_site_data import UrlsSiteData
from page_objects.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть страницу 'Лента заказов'")
    def open_order_feed_page(self):
        self.open_url(UrlsSiteData.ORDER_FEED_URL)

    @allure.step("Открыть модальное окно заказа")
    def open_order_modal(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER_BLOCK)

    @allure.step("Проверка отображения модального окна заказа")
    def is_modal_order_displayed(self):
        return self.is_element_displayed(OrderFeedPageLocators.MODAL_WINDOW_ORDER)

    @allure.step("Поиск заказа в ленте по номеру")
    def find_order_in_feed(self, order_number):
        self.wait.until(
            EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_FEED_LIST)
        )

        # Извлечение всех номеров заказов в ленте
        orders_in_feed_elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_FEED_LIST)
        order_numbers_in_feed = [order.text for order in orders_in_feed_elements if order.text.startswith("#")]

        # Проверка наличия искомого заказа
        return order_number in order_numbers_in_feed

    @allure.step("Получение количества выполненных заказов за всё время")
    def get_completed_total_orders_count(self):
        completed_count_text = self.get_text(OrderFeedPageLocators.ORDER_COMPLETED_TOTAL)
        return int(completed_count_text)

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_completed_today_orders_count(self):
        completed_count_text = self.get_text(OrderFeedPageLocators.ORDER_COMPLETED_TODAY)
        return int(completed_count_text)

    @allure.step("Проверка наличия заказа в разделе 'В работе'")
    def check_order_in_progress(self, order_number):
        return self.wait_for_condition(lambda d: self.is_order_in_progress(d, order_number))

    @allure.step("Проверка, что заказ в разделе 'В работе'")
    def is_order_in_progress(self, driver, order_number):
        # Извлекаем все заказы в разделе "В работе"
        orders_in_progress_elements = driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_PROGRESS)
        orders_in_progress = [element.text.lstrip("0") for element in
                              orders_in_progress_elements]  # Убираем ведущие нули

        # Проверка, что номер заказа присутствует в списке
        return order_number.lstrip("0") in orders_in_progress  # Убираем ведущие нули и из order_number для сравнения


