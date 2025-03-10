from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL
from locators import BUNS_SECTION, ACTIVE_BUNS_SECTION, SAUCES_SECTION, ACTIVE_SAUCES_SECTION, FILLINGS_SECTION, ACTIVE_FILLINGS_SECTION

def test_constructor_sections(driver):
    driver.get(MAIN_PAGE_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, BUNS_SECTION)))
    buns_tab = driver.find_element(By.XPATH, ACTIVE_BUNS_SECTION)
    assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class"), "Раздел 'Булки' не активен"
    sauces_tab = driver.find_element(By.XPATH, SAUCES_SECTION)
    sauces_tab.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, SAUCES_SECTION)))
    sauces_tab = driver.find_element(By.XPATH, ACTIVE_SAUCES_SECTION)
    assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class"), "Раздел 'Соусы' не активен"
    fillings_tab = driver.find_element(By.XPATH, FILLINGS_SECTION)
    fillings_tab.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, FILLINGS_SECTION)))
    fillings_tab = driver.find_element(By.XPATH, ACTIVE_FILLINGS_SECTION)
    assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class"), "Раздел 'Начинки' не активен"
    buns_tab = driver.find_element(By.XPATH, BUNS_SECTION)
    buns_tab.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, BUNS_SECTION)))
    buns_tab = driver.find_element(By.XPATH, ACTIVE_BUNS_SECTION)
    assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class"), "Раздел 'Булки' не активен"