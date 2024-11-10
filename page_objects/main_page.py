import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from data.urls_site_data import UrlsSiteData
from selenium.common.exceptions import ElementClickInterceptedException
from page_objects.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(UrlsSiteData.MAIN_URL)

    @allure.step("Ожидание загрузки главной страницы")
    def wait_main_page(self):
        self.wait_for_url(UrlsSiteData.MAIN_URL)

    @allure.step("Проверка перехода на главную страницу")
    def is_on_main_page(self):
        return self.is_current_url(UrlsSiteData.MAIN_URL)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_account_button(self):
        self.click(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверка отображения блока 'Соберите бургер'")
    def is_burger_header_displayed(self):
        return self.is_element_displayed(MainPageLocators.BURGER_TITLE)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.FEED_BUTTON)

    @allure.step("Клик по ингредиенту 'Флюоресцентная булка R2-D3'")
    def open_ingredient_modal(self):
        self.click(MainPageLocators.INGREDIENT_ITEM)

    @allure.step("Проверка открытие модального окна ингредиента")
    def is_modal_ingredient_displayed(self):
        return self.is_element_displayed(MainPageLocators.MODAL_INGREDIENT)

    @allure.step("Проверка закрытия модального окна ингредиента")
    def is_modal_ingredient_closed(self):
        return self.is_element_not_displayed(MainPageLocators.MODAL_INGREDIENT)

    @allure.step("Закрытие модального окна ингредиента")
    def close_modal_ingredient(self):
        self.click(MainPageLocators.MODAL_CLOSE_INGREDIENT_BUTTON)

    @allure.step("Перетаскиваем ингредиент в зону 'Выбранные ингредиенты'")
    def add_ingredient_to_order(self):
        ingredient = self.driver.find_element(*MainPageLocators.INGREDIENT_ITEM)
        droppable_area = self.driver.find_element(*MainPageLocators.DROPPABLE_AREA)

        # Используем ActionChains для перетаскивания
        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient).move_to_element(droppable_area).release().perform()

    @allure.step("Получение количества добавленных ингредиентов")
    def get_ingredient_count(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверка отображения модального окна 'Индикатор заказа'")
    def is_modal_order_displayed(self):
        return self.is_element_displayed(MainPageLocators.ORDER_INDICATOR_MODAL)

    @allure.step("Закрытие модального окна заказа")
    def close_modal_order(self):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.MODAL_CLOSE_ORDER_BUTTON)
        )

        # Проверяем, что кнопка закрытия не перекрыта и доступна для клика
        is_clicked = False
        while not is_clicked:
            try:
                # Пробуем кликнуть на кнопку
                self.driver.find_element(*MainPageLocators.MODAL_CLOSE_ORDER_BUTTON).click()
                is_clicked = True  # Если клик успешен, устанавливаем флаг
            except ElementClickInterceptedException:
                # Если элемент все еще перекрыт, ждем перед повторной попыткой
                self.wait.until(
                    EC.visibility_of_element_located(MainPageLocators.MODAL_CLOSE_ORDER_BUTTON)
                )

    @allure.step("Проверка отсутствия модального окна заказа")
    def is_modal_order_not_displayed(self):
        return self.is_element_not_displayed(MainPageLocators.ORDER_INDICATOR_MODAL)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        # Ожидание появления номера заказа в модальном окне
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_MODAL)
        )

        # Ожидание, пока номер заказа изменится с заглушки "9999" на другой номер
        order_number_element = self.driver.find_element(*MainPageLocators.ORDER_NUMBER_MODAL)
        self.wait.until(lambda driver: order_number_element.text != "9999")

        return order_number_element.text

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)







