from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локатор для кнопки "Личный кабинет" на главной странице
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/account']")

    # Локатор для кнопки “Конструктор” на странице авторизации
    CONSTRUCTOR_BUTTON = (
    By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Конструктор']]")

    # Проверка на наличие заголовка "Соберите бургер"
    BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Локатор для заголовка “Соберите бургер” на странице конструктора
    BUILD_BURGER_HEADER = (
    By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//h1[text()='Соберите бургер']")

    # Локатор для кнопки “Лента заказов” на главной странице
    FEED_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Лента Заказов']]")

    # Локатор для ингредиента “Флюоресцентная булка R2-D3”
    INGREDIENT_ITEM = (By.XPATH,
                       "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and .//p[text()='Флюоресцентная булка R2-D3']]")

    # Локатор для модального окна “Детали ингредиента”
    MODAL_INGREDIENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")

    # Локатор для кнопки закрытия (крестик) в модальном окне ингредиента
    MODAL_CLOSE_INGREDIENT_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    #Локатор для зоны «Выбранные ингредиенты»
    DROPPABLE_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")

    # Локатор для счетчика ингредиента
    INGREDIENT_COUNTER = (
    By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj')]//p[@class='counter_counter__num__3nue1']")

    # Локатор для кнопки “Оформить заказ”
    ORDER_BUTTON = (By.XPATH,
                    "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg')]")

    # Локатор для модального окна “Индикатор заказа”
    ORDER_INDICATOR_MODAL = (By.XPATH,
                             "//div[contains(@class, 'Modal_modal__container__')]")

    # Локатор для кнопки закрытия (крестик) в модальном окне заказа
    MODAL_CLOSE_ORDER_BUTTON = (By.XPATH,
    "//button[contains(@class, 'Modal_modal__close') and @type='button']")


    ORDER_NUMBER_MODAL = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'text_type_digits-large')]"
    )

    # Локатор для кнопки “Войти в аккаунт”
    LOGIN_BUTTON = (By.XPATH,
                    "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg')]")


