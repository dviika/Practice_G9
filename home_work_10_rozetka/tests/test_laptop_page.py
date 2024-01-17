import pytest
import time
import logging
from home_work_10_rozetka.main_rozetka_page.rozetka_laptops_page import LaptopPage
from home_work_10_rozetka.helper.laptop_page_helper import LaptopPageHelper


class TestLaptopPage:

    @pytest.mark.smoke
    def test_count_per_page(self, chrome):
        target_count = 60
        page = LaptopPage(chrome)
        helper = LaptopPageHelper(chrome)
        page.open()
        count_per_page = helper.get_count_per_page()
        assert target_count == count_per_page, "Target is NOT equal to items per page"

    @pytest.mark.smoke
    def test_scroll_down_to_element(self, chrome):
        page = LaptopPage(chrome)
        helper = LaptopPageHelper(chrome)
        page.open()
        pagination_1 = page.pagination_1()
        helper.scroll_down_to_element(pagination_1) #if no property page pagination is like method you can't take webelement methods
        assert pagination_1.is_enabled(), "Pagination 1 is not enabled"

        previous_button = page.previous_button()
        next_button = page.next_button()
        assert helper.is_button_disabled(previous_button), "Previous button is NOT disabled"
        assert helper.is_button_enabled(next_button), "Next button is not enabled"


    @pytest.mark.smoke
    def test_scroll_down_and_click_on_next(self, chrome):
        target_count_page2 = 60
        page = LaptopPage(chrome)
        helper = LaptopPageHelper(chrome)

        page.open()
        next_button = page.next_button()
        helper.scroll_down_to_element(next_button)
        helper.wait_till_element_clickable() #def to wait until elements are shown
        next_button.click()
        count_per_page = helper.get_count_per_page()

        assert target_count_page2 == count_per_page, "Target is NOT equal to items per page"
        pagination_2 = page.pagination_2()
        helper.scroll_down_to_element(pagination_2)
        helper.wait_till_element_present()
        assert helper.is_pagination_active(pagination_2), "Pagination 2 is not selected"
        assert 'page=2' in page.current_url(), "Title doesn't contain page 2 "
        logging.error('Logging level error check')

    @pytest.mark.regression
    def test_select_apple_laptops(self, chrome):
        page = LaptopPage(chrome)
        page.open()
        apple_checkbox = page.apple_checkbox()
        apple_checkbox.click()
        time.sleep(5)
        laptops = page.laptops_list()
        print(len(laptops)) #for checking whether we found all laptops
        logging.info('If laptops were printed most probably we are fine')
        for laptop in laptops:
            print(laptop.text)
            assert "Apple" in laptop.text, f"Title Apple is not found in {laptop.text}"
