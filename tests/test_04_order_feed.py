import pytest
import allure
from page_objects.main_page import MainPage
from page_objects.profile_page import ProfilePage
from page_objects.order_feed_page import OrderFeedPage


@allure.story("4. Раздел «Лента заказов»")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestOrderFeed:

    @allure.title("1. Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_order_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_order_feed_page()
        order_feed_page.open_order_modal()

        assert order_feed_page.is_modal_order_displayed(), "Модальное окно не открылось"

    @allure.title("2. Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_logged_in_user_order_history_visible_in_feed(self, driver, login_to_profile):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_to_profile()
        main_page.click_account_button()
        profile_page.go_to_order_history()
        last_order_number = profile_page.get_last_order_in_history()

        order_feed_page.open_order_feed_page()

        assert order_feed_page.find_order_in_feed(
            last_order_number), f"Заказ с номером {last_order_number} не найден в ленте заказов"

    @allure.title("3. При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_order_completion_total_counter_increases(self,driver, login_to_profile):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_order_feed_page()
        initial_completed_count = order_feed_page.get_completed_total_orders_count()

        login_to_profile()

        main_page.wait_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        main_page.is_modal_order_displayed()
        main_page.close_modal_order()
        main_page.click_order_feed()

        # Проверяем, что значение счётчика увеличилось
        updated_completed_count = order_feed_page.get_completed_total_orders_count()

        assert updated_completed_count > initial_completed_count, "Счётчик не увеличился после создания заказа"

    @allure.title("4. При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_completion_today_counter_increases(self,driver, login_to_profile):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_order_feed_page()
        initial_completed_count = order_feed_page.get_completed_today_orders_count()

        login_to_profile()

        main_page.wait_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        main_page.close_modal_order()
        main_page.click_order_feed()

        # Проверяем, что значение счётчика увеличилось
        updated_completed_count = order_feed_page.get_completed_today_orders_count()

        assert updated_completed_count > initial_completed_count, "Счётчик не увеличился после создания заказа"

    @allure.title("5. После оформления заказа его номер появляется в разделе В работе")
    def test_order_appears_in_progress_section_after_creation(self, driver, login_to_profile):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_to_profile()

        # Открываем второе окно для Ленты заказов
        main_page.open_new_window('https://stellarburgers.nomoreparties.site/feed')
        windows = main_page.get_window_handles()
        main_window = windows[0]
        feed_window = windows[1]

        # Оформляем заказ в первом окне
        main_page.switch_to_window(main_window)
        main_page.wait_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()

        # Извлекаем номер заказа из модального окна с ожиданием его появления
        order_number = main_page.get_order_number()

        # Переходим во второе окно с лентой заказов
        main_page.switch_to_window(feed_window)

        # Проверяем, что заказ появился в разделе "В работе"
        assert order_feed_page.check_order_in_progress(
            order_number), f"Заказ с номером {order_number} не найден в разделе 'В работе'"








