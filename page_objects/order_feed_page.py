import allure
from locators.order_feed_locators import OrderFeedPageLocators
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
        # Форматируем номер заказа с префиксом, если он используется в интерфейсе
        order_number_with_prefix = f"#{order_number.lstrip('#')}"

        # Убедимся, что список заказов виден
        self.wait_until_visible(OrderFeedPageLocators.ORDER_FEED_LIST)

        # Используем уже методы "is_text_in_elements" в BasePage для проверки текста в элементах
        return self.is_text_in_elements(OrderFeedPageLocators.ORDER_FEED_LIST, order_number_with_prefix)

    @allure.step("Проверка, что заказ в разделе 'В работе'")

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
        return self.wait_for_condition(lambda _: self.is_order_in_progress(order_number))

    @allure.step("Проверка, что заказ в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        # Извлекаем все заказы в разделе "В работе"
        orders_in_progress_elements = self.find_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS)
        orders_in_progress = [element.text.lstrip("0") for element in
                              orders_in_progress_elements]  # Убираем ведущие нули

        # Проверка, что номер заказа присутствует в списке
        return order_number.lstrip("0") in orders_in_progress  # Убираем ведущие нули и из order_number для сравнения
