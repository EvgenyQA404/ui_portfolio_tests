import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless=new")  # если нужно без UI
    drv = None
    try:
        drv = webdriver.Chrome(options=options)  # путей не указываем!
        drv.implicitly_wait(5)
        yield drv
    finally:
        if drv:
            drv.quit()
