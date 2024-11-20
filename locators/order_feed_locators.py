from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_FEED_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59')]//p[contains(@class, 'text_type_digits-default')]")

    FIRST_ORDER_BLOCK = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_list')]/li[contains(@class, 'OrderHistory_listItem')][1]//a[contains(@class, 'OrderHistory_link')]"
    )

    MODAL_WINDOW_ORDER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]"
    )

    ORDER_NUMBER_IN_FEED = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]")


    ORDER_COMPLETED_TOTAL = (By.XPATH, "//p[contains(@class, 'text_type_digits-large')]")

    ORDER_COMPLETED_TODAY = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )

    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[contains(@class, 'text_type_digits-default')]"
    )





