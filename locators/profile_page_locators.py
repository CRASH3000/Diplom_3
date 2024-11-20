from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Локатор для кнопки "История заказов" на странице профиля
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(@href, '/account/order-history') and contains(@class, 'Account_link')]")

    ORDER_HISTORY_LIST = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList__374GU')]//li")
    LAST_ORDER_NUMBER = (By.XPATH,
                         "//ul[contains(@class, 'OrderHistory_profileList__374GU')]//li[last()]//p[contains(@class, 'text_type_digits-default')]")

    # Локатор для кнопки "Выход" на странице профиля
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")