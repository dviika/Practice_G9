from selenium.common import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from home_work_10_rozetka.locators import locators


class LaptopPage:
    URL = 'https://rozetka.com.ua/ua/notebooks/c80004/'

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def open(self):
        self.__driver.get(self.URL)
        return self

    def current_url(self):
        return self.__driver.current_url

    def pagination_1(self):
        return self.__driver.find_element(By.XPATH, locators.first_pagination_locator)

    def pagination_2(self):
        return self.__driver.find_element(By.XPATH, locators.second_paginator_locator)

    def previous_button(self):
        return self.__driver.find_element(By.XPATH, locators.previous_btn_at_the_bottom_locator)

    def next_button(self):
        return self.__driver.find_element(By.XPATH, locators.next_btn_at_the_bottom_locator)

    def laptops_list(self):
        return self.__driver.find_elements(By.XPATH, locators.laptop_list_item)

    def apple_checkbox(self):
        return self.__driver.find_element(By.XPATH, locators.checkbox_apple)
