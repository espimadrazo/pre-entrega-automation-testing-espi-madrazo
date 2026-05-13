from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login


# CATALOG PAGE TITLE VALIDATION
def test_inventory_page_title(driver):

    wait = WebDriverWait(driver, 8)

    login(driver, "standard_user","secret_sauce")


    title = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    ).text

    assert title == "Products"


# CHECK PRESENCE OF AT LEAST 1 PRODUCT
def test_product_presence(driver):
    wait = WebDriverWait(driver, 8)

    login(driver, "standard_user","secret_sauce")

    products = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test = 'inventory-item']"))
    )

    assert len(products) >= 1

    # Checks presence of title and price
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_price"))
    )


# CHECK PRESENCE OF MAIN ELEMENTS: SIDE MENU
def test_menu_presence(driver):
    wait = WebDriverWait(driver, 8)

    login(driver, "standard_user","secret_sauce")

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "bm-menu"))
    )


# CHECK PRESENCE OF MAIN ELEMENTS: FILTERS
def test_menu_presence(driver):
    wait = WebDriverWait(driver, 8)

    login(driver, "standard_user","secret_sauce")

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )

# CHECK PRESENCE OF MAIN ELEMENTS: FOOTER
def test_menu_presence(driver):
    wait = WebDriverWait(driver, 8)

    login(driver, "standard_user","secret_sauce")

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "footer"))
    )