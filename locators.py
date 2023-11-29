from selenium.webdriver.common.by import By

class Locators:
    TO_REG_PAGE_LINK = By.XPATH, "//*[contains(@href, 'register')]" # Ссылка для перехода в форму регистрации
    NAME_FIELD = By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input" # Поле "Имя"
    EMAIL_FIELD = By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input" # Поле "Email"
    PASSWORD_FIELD = By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input" # Поле "Пароль"
    REGISTER_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"
    INVALID_PASS_TEXT = By.XPATH, "//*[contains(@class, 'input__error')]" # Текст "Некорректный пароль"
    TO_LOGIN_PAGE_BUTTON = By.XPATH, "//*[contains(@class, 'button_button_size_large')]" # Кнопка "Войти в аккаунт" на главной
    TO_ACCOUNT_PAGE_BUTTON = By.XPATH, "//*[contains(@href, 'account')]" # Кнопка "Личный кабинет"
    LOGIN_BUTTON = By.XPATH, "//*[contains(@class, 'button_button_size_medium')]" # Кнопка "Войти"
    TO_ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'button_button_size_large')]" # Кнопка "Оформить заказ" на главной
    TO_LOGIN_PAGE_LINK = By.XPATH, "//*[contains(@href, 'login')]" # Ссылка для перехода в форму авторизации
    TO_PASS_RECOVERY_PAGE_LINK = By.XPATH, "//*[contains(@href, 'forgot-password')]" # Ссылка для перехода в форму восстановления пароля
    TO_CONSTRUCTOR_BUTTON = By.XPATH, "//nav/ul/li[1]//p[contains(@class, 'AppHeader_header__linkText')]" # Кнопка "Конструктор" в навигационном меню
    LOGO_BUTTON = By.XPATH, "//nav/div/a[@href='/']" # Кнопка Лого в навигационном меню
    LOGOUT_BUTTON = By.XPATH, "//ul/li[3]/button" # Кнопка "Выход" в личном кабинете
    BUNS_SECTION = By.XPATH, "//section/div/div[1]" # Раздел конструктора "Булки"
    SAUCES_SECTION = By.XPATH, "//section/div/div[2]"  # Раздел конструктора "Соусы"
    TOPPINGS_SECTION = By.XPATH, "//section/div/div[3]"  # Раздел конструктора "Начинки"
    CURRENT_SECTION = By.XPATH, "//section/div/div[contains(@class, 'current')]"  # Текущий раздел конструктора