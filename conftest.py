import pytest
from utils.helpers import install_driver

@pytest.fixture
def driver():
    driver = install_driver()
    yield driver
    driver.quit()
