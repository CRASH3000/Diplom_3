import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверка соответствия URL: {expected_url}")
    def is_current_url(self, expected_url):
        try:
            self.wait.until(EC.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста: {text}")
    def enter_text(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    @allure.step("Ожидание загрузки страницы: {url}")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step("Проверка активности элемента")
    def is_element_active(self, locator, active_class="input_status_active"):
        element = self.driver.find_element(*locator)
        return self.wait.until(lambda driver: active_class in element.get_attribute("class"))

    @allure.step("Проверка отображения элемента")
    def is_element_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    @allure.step("Проверка, что элемент не отображается")
    def is_element_not_displayed(self, locator):
        # Ожидание, пока модальное окно не исчезнет
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True  # Если элемент не появился в течение 10 секунд, возвращаем True
        except TimeoutException:
            return False # Если элемент появился, возвращаем False

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Получение списка текста элементов")
    def get_elements_text_list(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return [element.text for element in elements]

    @allure.step("Ожидание выполнения условия")
    def wait_for_condition(self, condition, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(condition)
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание видимости элемента")
    def wait_until_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

