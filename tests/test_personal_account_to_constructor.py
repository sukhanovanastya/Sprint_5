from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL, LOGIN_PAGE_URL, PERSONAL_ACCOUNT_URL
from locators import PERSONAL_ACCOUNT_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_BUTTON_AUTH

def test_go_to_personal_account_from_main_page(driver):
    driver.get(MAIN_PAGE_URL)

    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_PAGE_URL)
    )

    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123456")

    driver.find_element(By.XPATH, LOGIN_BUTTON_AUTH).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(MAIN_PAGE_URL)
    )

    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(PERSONAL_ACCOUNT_URL)
    )

    assert driver.current_url == PERSONAL_ACCOUNT_URL