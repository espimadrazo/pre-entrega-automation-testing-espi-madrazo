from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login

# LOGIN TEST
def test_login(driver):
    login(driver, "standard_user","secret_sauce")

# CHECK INVENTORY PAGE AFTER LOGIN
def test_inventory(driver):
    login(driver, "standard_user","secret_sauce")

    assert "inventory.html" in driver.current_url
