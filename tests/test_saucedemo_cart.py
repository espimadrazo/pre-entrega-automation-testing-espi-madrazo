from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login


# ADD PRODUCT TO CART
def test_add_product_to_cart(driver):

    wait = WebDriverWait(driver, 8)

    login(driver, "standard_user","secret_sauce")

    catalog_product = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        ).text

    # Locate and execute "Add to cart" button
    add_button = wait.until(
         EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Add to cart')]"))
    )

    add_button.click()

    # Check cart counter on header icon
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    # Browse to cart page
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        ).click()
    
    assert "cart.html" in driver.current_url

    # Check presence of correct added product in cart
    cart_product = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text

    assert cart_product == catalog_product