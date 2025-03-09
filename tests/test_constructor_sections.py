from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_constructor_sections(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))
    )

    buns_tab = driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div")
    assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class"), "Раздел 'Булки' не активен"

    sauces_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']")
    sauces_tab.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']"))
    )

    sauces_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div")
    assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class"), "Раздел 'Соусы' не активен"

    fillings_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']")
    fillings_tab.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']"))
    )

    fillings_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div")
    assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class"), "Раздел 'Начинки' не активен"

    buns_tab = driver.find_element(By.XPATH, "//span[text()='Булки']")
    buns_tab.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))
    )

    buns_tab = driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div")
    assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class"), "Раздел 'Булки' не активен"