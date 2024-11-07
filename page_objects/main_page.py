from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from data.urls_site_data import UrlsSiteData
from selenium.common.exceptions import ElementClickInterceptedException

class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_main_page(self):
        self.driver.get(UrlsSiteData.MAIN_URL)

    def wait_main_page(self):
        self.wait.until(
            EC.url_to_be(UrlsSiteData.MAIN_URL)
        )

    def click_account_button(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)
        ).click()

    def click_constructor(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        ).click()

    def is_burger_header_displayed(self):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE)
        )
        return self.driver.find_element(*MainPageLocators.BURGER_TITLE).is_displayed()

    def click_order_feed(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.FEED_BUTTON)
        ).click()

    def open_ingredient_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT_ITEM)
        ).click()

    def is_modal_ingredient_displayed(self):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.MODAL_INGREDIENT)
        )
        return self.driver.find_element(*MainPageLocators.MODAL_INGREDIENT).is_displayed()

    def is_modal_ingredient_closed(self):
        # Ожидание, пока модальное окно не исчезнет
        self.wait.until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_INGREDIENT)
        )
        return True

    def close_modal_ingredient(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_INGREDIENT_BUTTON)
        ).click()

    def add_ingredient_to_order(self):
        ingredient = self.driver.find_element(*MainPageLocators.INGREDIENT_ITEM)
        droppable_area = self.driver.find_element(*MainPageLocators.DROPPABLE_AREA)

        # Используем ActionChains для перетаскивания
        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient).move_to_element(droppable_area).release().perform()

    def get_ingredient_count(self):
        count_element = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER)
        )
        return int(count_element.text)

    def click_order_button(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        ).click()

    def is_modal_order_displayed(self):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_INDICATOR_MODAL)
        )
        return self.driver.find_element(*MainPageLocators.ORDER_INDICATOR_MODAL).is_displayed()

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


    def is_modal_order_not_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.ORDER_INDICATOR_MODAL)
            )
            return False  # Если элемент появился, возвращаем False
        except TimeoutException:
            return True  # Если элемент не появился в течение 10 секунд, возвращаем True

    def get_order_number(self):
        # Ожидание появления номера заказа в модальном окне
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_MODAL)
        )

        # Ожидание, пока номер заказа изменится с заглушки "9999" на другой номер
        order_number_element = self.driver.find_element(*MainPageLocators.ORDER_NUMBER_MODAL)
        self.wait.until(lambda driver: order_number_element.text != "9999")

        return order_number_element.text

    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()







