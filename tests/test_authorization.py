from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_via_main_page_login_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_login_via_personal_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, "//a[@href='/account']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_login_via_registration_form_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, "//a[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_login_via_password_recovery_form_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    driver.find_element(By.XPATH, "//a[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"