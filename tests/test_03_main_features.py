import pytest
import allure
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from data.urls_site_data import UrlsSiteData

@allure.story("3. Проверка основного функционала")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestMainFeatures:

    @allure.title("1. Переход по клику на «Конструктор»,")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        login_page.open_login_page()
        main_page.click_constructor()

        # Проверка URL
        assert driver.current_url == UrlsSiteData.MAIN_URL
        # Проверка на наличие заголовка "Соберите бургер"
        assert main_page.is_burger_header_displayed(), "Элемент 'Соберите бургер' не найден на странице"

    @allure.title("2. Переход по клику на «Лента заказов»")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_order_feed()

        assert driver.current_url == UrlsSiteData.ORDER_FEED_URL

    @allure.title("3. Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()

        # Клик по ингредиенту
        main_page.open_ingredient_modal()

        assert main_page.is_modal_ingredient_displayed(), "Модальное окно не открылось"

    @allure.title("4. Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.open_ingredient_modal()
        main_page.close_modal_ingredient()

        assert main_page.is_modal_ingredient_closed(), "Модальное окно не закрылось"

    @allure.title("5. При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.add_ingredient_to_order()

        assert main_page.get_ingredient_count() == 2, "Счетчик ингредиента не увеличился до 2"

    @allure.title("6. Залогиненный пользователь может оформить заказ.")
    def test_logged_in_user_can_place_order (self,driver, login_to_profile):
        main_page = MainPage(driver)

        login_to_profile()

        main_page.wait_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()

        assert main_page.is_modal_order_displayed(), "Модальное окно не открылось"

    @allure.title("7. Не залогиненный пользователь может оформить заказ.")
    def test_guest_user_cannot_place_order (self,driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_login_button()

        assert driver.current_url == UrlsSiteData.LOGIN_URL









