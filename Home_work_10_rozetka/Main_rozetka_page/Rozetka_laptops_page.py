from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Home_work_10_rozetka.Main_rozetka_page import locators


class Laptop_page:
    URL = 'https://rozetka.com.ua/ua/notebooks/c80004/'
    first_pagination_locator = '//li[@class="pagination__item"]/a[contains(@class,"pagination__link pagination__link--active")]'
    # previous_btn_at_the_bottom_locator = '//div[@class="pagination ng-star-inserted"]/a[contains(@title,"До попередньої сторінки")]' #'//div[@class="pagination ng-star-inserted"]/a[contains(@class,"button button--gray button")]'
    # next_btn_at_the_bottom_locator = '//div[@class="pagination ng-star-inserted"]/a[contains(@title,"До наступної сторінки")]' #'//div[@class="pagination ng-star-inserted"]/a[contains(@class,"pagination__direction--forward")]'

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def open(self):
        self.__driver.get(self.URL)
        return self

    @property
    def pagination_1(self):
        return self.__driver.find_element(By.XPATH, self.first_pagination_locator)

    @property
    def pagination_2(self):
        return self.__driver.find_element(By.XPATH, self.second_paginator_locator)

    @property
    def previous_button(self):
        return self.__driver.find_element(By.XPATH, locators.previous_btn_at_the_bottom_locator)

    @property
    def next_button(self):
        return self.__driver.find_element(By.XPATH, locators.next_btn_at_the_bottom_locator)

    def get_count_per_page(self, target_count):
        locator = '//img[contains(@class,"lazy_img_hover")]'  # finding 60 per page
        elements = self.__driver.find_elements(By.XPATH, locator)
        count_per_page = 0
        for _ in elements:
            count_per_page = count_per_page + 1

        return count_per_page

    def scroll_down_to_element(self, element):
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).perform()

    def is_previous_btn_disabled(self):
        prev_btn_enabled = self.previous_button.get_attribute('class')
        if 'disabled' in prev_btn_enabled:
            return True
        else:
            return False

    def is_next_button_enabled(self):
        next_btn_enabled = self.next_button.is_enabled()
        return next_btn_enabled


