import pytest
from locators import Locators
from helpers import Urls
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Фикстура на открытие браузера
@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1280,800')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()

# Фикстура на логин
@pytest.fixture
def login(driver):
    driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()

    driver.find_element(*Locators.EMAIL_FIELD).send_keys('praktikum_user765@ya.ru')
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
