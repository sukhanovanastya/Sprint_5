from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Иван Иванов")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("123456")

    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Иван Иванов")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ivan@yandex.ru")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("12345")

    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"))
    )

    assert error_message.text == "Некорректный пароль"