import random


class Generators:
    def __init__(self):
        self.login = self.login_generator()
        self.password = self.password_generator()

    # Функция генерации логина
    def login_generator(self):
        self.login = f'praktikum_user{random.randint(100,999)}@ya.ru'
        return self.login

    # Функция генерации пароля
    def password_generator(self):
        self.password = f'{random.randint(100000,999999)}'
        return self.password