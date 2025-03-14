from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import REGISTRATION_PAGE_URL, LOGIN_PAGE_URL
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, ERROR_MESSAGE

def test_successful_registration(driver):
    driver.get(REGISTRATION_PAGE_URL)
    driver.find_element(By.XPATH, NAME_INPUT).send_keys("Иван Иванов")
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123456")
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
    assert driver.current_url == LOGIN_PAGE_URL

def test_registration_with_invalid_password(driver):
    driver.get(REGISTRATION_PAGE_URL)
    driver.find_element(By.XPATH, NAME_INPUT).send_keys("Иван Иванов")
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("12345")
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE)))
    assert error_message.text == "Некорректный пароль"