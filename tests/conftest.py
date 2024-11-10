import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data.test_data import TestUserData
from page_objects.login_page import LoginPage
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: chrome или firefox")

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser = request.param
    with allure.step(f"Запуск теста в браузере {browser}"):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        elif browser == "firefox":

            # Вариант 1: Используем GeckoDriverManager для автоматической загрузки драйвера
            firefox_options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

            # Вариант 2: Запасной вариант с указанием прямого пути к geckodriver
            # geckodriver_path = "/usr/local/bin/geckodriver"
            # driver = webdriver.Firefox(service=FirefoxService(executable_path=geckodriver_path), options=firefox_options)
        else:
            raise ValueError(f"Браузер {browser} не поддерживается. Используйте 'chrome' или 'firefox'.")

        driver.maximize_window()
        yield driver
        driver.quit()


@pytest.fixture
def login_to_profile(driver):
    def login(email=TestUserData.TEST_EMAIL, password=TestUserData.TEST_PASSWORD):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()

    return login