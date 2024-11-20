import pytest
import allure
from page_objects.login_page import LoginPage
from data.urls_site_data import UrlsSiteData
from data.test_data import TestUserData

@allure.story("1. Восстановление пароля")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestRestorePassword:

    @allure.title("1. Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_restore_password_page(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.click_restore_password_button()

        assert page.is_current_url(UrlsSiteData.FORGOT_PASSWORD_URL), "Не удалось перейти на страницу восстановления пароля"

    @allure.title("2. Ввод почты и клик по кнопке «Восстановить»")
    def test_restore_password_functionality(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.click_restore_password_button()
        page.enter_email(TestUserData.TEST_EMAIL)
        page.click_restore_button()
        page.wait_restore_password_page()

        assert page.is_current_url(UrlsSiteData.RESET_PASSWORD_URL), "Не удалось перейти на страницу с вводом пароля и кода из письма"


    @allure.title("3. Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_toggle_password_field_activation(self, driver):
        page = LoginPage(driver)
        page.open_restore_password_page()
        page.click_restore_button()
        page.enter_password(TestUserData.TEST_PASSWORD)
        page.click_toggle_password_visibility()

        assert page.is_password_field_active(), "Поле пароля не активировалось после нажатия на кнопку показа пароля"