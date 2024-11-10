class UrlsSiteData:
    BASE_URL = "https://stellarburgers.nomoreparties.site" # Она же и страница с конструктором заказа

    MAIN_URL = f"{BASE_URL}/" # Главная страница
    ORDER_FEED_URL = f"{BASE_URL}/feed"
    LOGIN_URL = f"{BASE_URL}/login"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_URL = f"{BASE_URL}/reset-password"
    PROFILE_URL = f"{BASE_URL}/account/profile"
    ORDER_HISTORY_URL = f"{BASE_URL}/account/order-history"