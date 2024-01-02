import pytest
from selenium import webdriver
import undetected_chromedriver as webdriver

@pytest.fixture()
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--use_subprocess")
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
    yield driver
    driver.quit()
