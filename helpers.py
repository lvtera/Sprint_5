import random

class Urls:
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/' # Адрес главной страницы
    LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login' # Адрес страницы авторизации
    PERSONAL_ACCOUNT_URL = 'https://stellarburgers.nomoreparties.site/account/profile' # Адрес страницы личного кабинета

class Generators:
    def __init__(self):
        self.login = ''
        self.password = ''

    # Функция генерации логина
    def login_generator(self):
        self.login = f'praktikum_user{random.randint(100,999)}@ya.ru'
        return self.login

    # Функция генерации пароля
    def password_generator(self):
        self.password = f'{random.randint(100000,999999)}'
        return self.password