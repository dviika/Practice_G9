from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Home_work_10_rozetka.Main_rozetka_page import locators

class Laptop_page:
    URL = 'https://rozetka.com.ua/ua/notebooks/c80004/'

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def open(self):
        self.__driver.get(self.URL)
        return self

    def current_url(self):
        return self.__driver.current_url

    @property
    def pagination_1(self):
        return self.__driver.find_element(By.XPATH, locators.first_pagination_locator)

    @property
    def pagination_2(self):
        return self.__driver.find_element(By.XPATH, locators.second_paginator_locator)

    @property
    def previous_button(self):
        return self.__driver.find_element(By.XPATH, locators.previous_btn_at_the_bottom_locator)

    @property
    def next_button(self):
        return self.__driver.find_element(By.XPATH, locators.next_btn_at_the_bottom_locator)

    @property
    def laptops_list(self):
        return self.__driver.find_elements(By.XPATH, locators.laptop_list_item)

    @property
    def apple_checkbox(self):
        return self.__driver.find_element(By.XPATH,locators.checkbox_apple)


    def get_count_per_page(self):
        locator = '//img[contains(@class,"lazy_img_hover")]'  # finding 60 per page
        elements = self.__driver.find_elements(By.XPATH, locator)
        count_per_page = len(elements)
        return count_per_page

    def scroll_down_to_element(self, element):
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).perform()

    def wait_till_element_clickable(self):
        try:
            myElem = WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.next_btn_at_the_bottom_locator)))
            print("Element_is located")
        except TimeoutException:
            print("Loading took too much time!")


    def wait_till_element_present(self):
        try:
            myElem = WebDriverWait(self.__driver, 10).until(EC.text_to_be_present_in_element_attribute((By.XPATH, locators.second_paginator_locator),
                                                            attribute_='class', text_='active'))
            print("Text_is_present_in_element_attribute")
        except TimeoutException:
            print("Loading took too much time!")


    def is_pagination2_active(self):
        class_name = self.pagination_2.get_attribute("class")
        print("Pagination_2 class name: ", class_name)
        if 'active' in class_name:
            return True
        else:
            return False

    def is_previous_btn_disabled(self):
        prev_btn_enabled = self.previous_button.get_attribute('class')
        if 'disabled' in prev_btn_enabled:
            return True
        else:
            return False

    def is_next_button_enabled(self):
        next_btn_enabled = self.next_button.is_enabled()
        return next_btn_enabled


