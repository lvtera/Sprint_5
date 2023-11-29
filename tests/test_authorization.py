from locators import Locators
from data import AuthData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthorization:

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_authorization_login_button(self, driver):
        driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()

        driver.find_element(*Locators.EMAIL_FIELD).send_keys(AuthData.login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(AuthData.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
        button_text = driver.find_element(*Locators.TO_ORDER_BUTTON).text

        assert button_text == 'Оформить заказ'

    # Вход через кнопку «Личный кабинет»
    def test_authorization_account_button(self, driver):
        driver.find_element(*Locators.TO_ACCOUNT_PAGE_BUTTON).click()

        driver.find_element(*Locators.EMAIL_FIELD).send_keys(AuthData.login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(AuthData.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
        button_text = driver.find_element(*Locators.TO_ORDER_BUTTON).text

        assert button_text == 'Оформить заказ'

    # Вход через кнопку в форме регистрации
    def test_authorization_from_reg_page(self, driver):
        driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.TO_REG_PAGE_LINK).click()
        driver.find_element(*Locators.TO_LOGIN_PAGE_LINK).click()

        driver.find_element(*Locators.EMAIL_FIELD).send_keys(AuthData.login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(AuthData.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
        button_text = driver.find_element(*Locators.TO_ORDER_BUTTON).text

        assert button_text == 'Оформить заказ'

    # Вход через кнопку в форме восстановления пароля
    def test_authorization_from_pass_recovery_page(self, driver):
        driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.TO_PASS_RECOVERY_PAGE_LINK).click()
        driver.find_element(*Locators.TO_LOGIN_PAGE_LINK).click()

        driver.find_element(*Locators.EMAIL_FIELD).send_keys(AuthData.login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(AuthData.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
        button_text = driver.find_element(*Locators.TO_ORDER_BUTTON).text

        assert button_text == 'Оформить заказ'
