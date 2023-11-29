from locators import Locators
from helpers import Urls
from helpers import Generators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    # Тест на успешную регистрацию с валидными данными
    def test_registration_valid_data(self, driver):
        driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.TO_REG_PAGE_LINK).click()

        user = Generators()

        driver.find_element(*Locators.NAME_FIELD).send_keys('Anna')
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user.login_generator())
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(user.login_generator())
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.LOGIN_PAGE_URL))

        assert driver.current_url == Urls.LOGIN_PAGE_URL

    # Тест на ошибку при регистрации с паролем менее 6 символов
    def test_registration_short_password(self, driver):
        driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.TO_REG_PAGE_LINK).click()

        user = Generators()

        driver.find_element(*Locators.NAME_FIELD).send_keys('Anna')
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user.login_generator())
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.INVALID_PASS_TEXT))

        assert driver.find_element(*Locators.INVALID_PASS_TEXT).text == 'Некорректный пароль'
