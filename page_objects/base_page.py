import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

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

    @allure.step("Найти элемент по локатору")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти элементы по локатору")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Перетаскивание элемента из источника в цель")
    def drag_and_drop(self, ingredient_locator, droppable_area_locator):
        ingredient = self.find_element(ingredient_locator)
        droppable_area = self.find_element(droppable_area_locator)

        # Используем ActionChains для перетаскивания
        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient).move_to_element(droppable_area).release().perform()

    @allure.step("Получение текста всех элементов из писка по локатору")
    def get_elements_text(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return [element.text for element in elements]

    @allure.step("Проверка, что текст '{text}' присутствует в списке элементов")
    def is_text_in_elements(self, locator, text):
        # Получаем текст всех элементов, соответствующих локатору
        elements_text = self.get_elements_text(locator)

        # Проверяем, содержится ли нужный текст в списке элементов
        return any(text == element_text.strip() for element_text in elements_text)

    @allure.step("Открытие нового окна с URL: {url}")
    def open_new_window(self, url):
        self.driver.execute_script(f"window.open('{url}', '_blank');")

    @allure.step("Получение списка всех окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключение на окно")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Закрытие оверлея, если он присутствует")
    def close_overlay_if_present(self, locator):
        try:
            overlay = self.wait.until(EC.visibility_of_element_located(locator))
            overlay.click()
        except TimeoutException:
            pass  # Оверлей не отображается

