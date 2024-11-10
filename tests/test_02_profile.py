import pytest
import allure
from page_objects.profile_page import ProfilePage
from page_objects.main_page import MainPage
from data.urls_site_data import UrlsSiteData


@allure.story("2. Личный кабинет")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestProfile:

    @allure.title("1. Переход по клику на «Личный кабинет»")
    def test_navigate_to_account(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_account_button()

        assert main_page.is_current_url(UrlsSiteData.LOGIN_URL), "Не удалось перейти на страницу авторизации"

    @allure.title("2. Переход в раздел «История заказов»")
    def test_order_history_access(self, driver, login_to_profile):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_main_page()
        main_page.click_account_button()

        # Авторизация
        login_to_profile()
        main_page.wait_main_page()

        assert main_page.is_on_main_page(), "Не удалось войти в систему"

        main_page.click_account_button()
        profile_page.go_to_order_history()

        assert profile_page.is_current_url(UrlsSiteData.ORDER_HISTORY_URL), "Не удалось перейти в раздел История заказов"

    @allure.title("3. Выход из аккаунта.")
    def test_logout(self, driver, login_to_profile):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_main_page()
        main_page.click_account_button()

        login_to_profile()

        main_page.wait_main_page()
        assert main_page.is_on_main_page(), "Не удалось войти в систему"

        main_page.click_account_button()
        profile_page.logout()

        assert profile_page.is_current_url(UrlsSiteData.PROFILE_URL), "Не удалось выйти из аккаунта"