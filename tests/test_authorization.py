from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL, LOGIN_PAGE_URL, FORGOT_PASSWORD_URL, REGISTRATION_PAGE_URL
from locators import LOGIN_BUTTON_MAIN_PAGE, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_BUTTON_AUTH, PERSONAL_ACCOUNT_BUTTON, LOGIN_BUTTON_FORGOT_PASSWORD

def test_login_via_main_page_login_button(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN_PAGE).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123456")
    driver.find_element(By.XPATH, LOGIN_BUTTON_AUTH).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))
    assert driver.current_url == MAIN_PAGE_URL

def test_login_via_personal_account_button(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123456")
    driver.find_element(By.XPATH, LOGIN_BUTTON_AUTH).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))
    assert driver.current_url == MAIN_PAGE_URL

def test_login_via_registration_form_button(driver):
    driver.get(REGISTRATION_PAGE_URL)
    driver.find_element(By.XPATH, LOGIN_BUTTON_FORGOT_PASSWORD).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123456")
    driver.find_element(By.XPATH, LOGIN_BUTTON_AUTH).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))
    assert driver.current_url == MAIN_PAGE_URL

def test_login_via_password_recovery_form_button(driver):
    driver.get(FORGOT_PASSWORD_URL)
    driver.find_element(By.XPATH, LOGIN_BUTTON_FORGOT_PASSWORD).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123456")
    driver.find_element(By.XPATH, LOGIN_BUTTON_AUTH).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))
    assert driver.current_url == MAIN_PAGE_URL