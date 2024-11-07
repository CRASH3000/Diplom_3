from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from locators.order_feed_locators import OrderFeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls_site_data import UrlsSiteData

class OrderFeedPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_order_feed_page(self):
        self.driver.get(UrlsSiteData.ORDER_FEED_URL)

    def open_order_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(OrderFeedPageLocators.FIRST_ORDER_BLOCK)
        ).click()

    def is_modal_order_displayed(self):
        # Ожидание, пока модальное окно не станет видимым
        self.wait.until(
            EC.visibility_of_element_located(OrderFeedPageLocators.MODAL_WINDOW_ORDER)
        )
        return self.driver.find_element(*OrderFeedPageLocators.MODAL_WINDOW_ORDER).is_displayed()

    def find_order_in_feed(self, order_number):
        self.wait.until(
            EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_FEED_LIST)
        )

        # Извлечение всех номеров заказов в ленте
        orders_in_feed_elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_FEED_LIST)
        order_numbers_in_feed = [order.text for order in orders_in_feed_elements if order.text.startswith("#")]

        # Проверка наличия искомого заказа
        return order_number in order_numbers_in_feed

    def get_completed_total_orders_count(self):
        self.wait.until(
            EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_COMPLETED_TOTAL)
        )
        # Извлекаем текст из элемента и преобразуем его в целое число
        completed_count_text = self.driver.find_element(*OrderFeedPageLocators.ORDER_COMPLETED_TOTAL).text
        return int(completed_count_text)

    def get_completed_today_orders_count(self):
        self.wait.until(
            EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_COMPLETED_TODAY)
        )
        completed_count_text = self.driver.find_element(*OrderFeedPageLocators.ORDER_COMPLETED_TODAY).text
        return int(completed_count_text)

    def check_order_in_progress(self, order_number):
        # Увеличиваем таймаут и добавляем промежуточные проверки с отладочными сообщениями
        timeout = 30  # увеличено время ожидания до 30 секунд
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.is_order_in_progress(d, order_number),
                f"Заказ с номером {order_number} не найден в разделе 'В работе'"
            )
            return True  # Возвращаем True, если заказ найден
        except TimeoutException:
            return False  # Возвращаем False, если заказ не найден за отведенное время

    def is_order_in_progress(self, driver, order_number):
        # Извлекаем все заказы в разделе "В работе"
        orders_in_progress_elements = driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_PROGRESS)
        orders_in_progress = [element.text.lstrip("0") for element in
                              orders_in_progress_elements]  # Убираем ведущие нули

        # Проверка, что номер заказа присутствует в списке
        return order_number.lstrip("0") in orders_in_progress  # Убираем ведущие нули и из order_number для сравнения


