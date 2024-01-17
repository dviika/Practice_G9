from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from home_work_10_rozetka.locators import locators


class LaptopPageHelper:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def scroll_down_to_element(self, element):
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).perform()

    def get_count_per_page(self):
        elements = self.__driver.find_elements(By.XPATH, locators.laptop_images_per_default)
        count_per_page = len(elements)
        return count_per_page

    def is_pagination_active(self, pagination):
        class_name = pagination.get_attribute("class")
        print("Pagination_2 class name: ", class_name)
        if 'active' in class_name:
            return True
        else:
            return False

    def is_button_disabled(self, button):
        button_enabled = button.get_attribute('class')
        if 'disabled' in button_enabled:
            return True
        else:
            return False

    def is_button_enabled(self, button):
        button_enabled = button.is_enabled()
        return button_enabled

    def wait_till_element_clickable(self):
        try:
            myElem = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locators.next_btn_at_the_bottom_locator)))
            print("Element_is located")
        except TimeoutException:
            print("Loading took too much time!")

    def wait_till_element_present(self):
        try:
            myElem = WebDriverWait(self.__driver, 10).until(
                EC.text_to_be_present_in_element_attribute((By.XPATH, locators.second_paginator_locator),
                                                           attribute_='class', text_='active'))
            print("Text_is_present_in_element_attribute")
        except TimeoutException:
            print("Loading took too much time!")
