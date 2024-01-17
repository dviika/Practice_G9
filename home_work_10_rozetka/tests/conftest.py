import pytest
from selenium.webdriver import Chrome
import undetected_chromedriver as webdriver

@pytest.fixture(scope = 'session')
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--use_subprocess")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


