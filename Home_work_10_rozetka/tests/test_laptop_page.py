import pytest
import time
import logging
from Home_work_10_rozetka.Main_rozetka_page.Rozetka_laptops_page import Laptop_page


class TestLaptopPage:

    @pytest.mark.smoke
    def test_count_per_page(self, chrome):
        target_count = 60
        page = Laptop_page(chrome)
        page.open()
        count_per_page = page.get_count_per_page()
        assert target_count == count_per_page, "Target is NOT equal to items per page"

    @pytest.mark.smoke
    def test_scroll_down_to_element(self, chrome):
        page = Laptop_page(chrome)
        page.open()
        page.scroll_down_to_element(page.pagination_1) #if no property page pagination is like method you can't take webelement methods
        assert page.pagination_1.is_enabled(), "Pagination 1 is not enabled"
        assert page.is_previous_btn_disabled(), "Previous button is NOT disabled"
        assert page.is_next_button_enabled(), "Next button is not enabled"


    @pytest.mark.smoke
    def test_scroll_down_and_click_on_next(self, chrome):
        target_count_page2 = 60
        page = Laptop_page(chrome)
        page.open()
        page.scroll_down_to_element(page.next_button)
        page.wait_till_element_clickable() #def to wait until elements are shown
        page.next_button.click()
        count_per_page = page.get_count_per_page()
        assert target_count_page2 == count_per_page, "Target is NOT equal to items per page"
        page.scroll_down_to_element(page.pagination_2)
        page.wait_till_element_present()
        assert page.is_pagination2_active(), "Pagination 2 is not selected"
        assert 'page=2' in page.current_url(), "Title doesn't contain page 2 "
        logging.error('Logging level error check')

    @pytest.mark.regression
    def test_select_apple_laptops(self, chrome):
        page = Laptop_page(chrome)
        page.open()
        page.apple_checkbox.click()
        time.sleep(5)
        laptops = page.laptops_list
        print(len(laptops)) #for checking whether we found all laptops
        logging.info('If laptops were printed most probably we are fine')
        for laptop in laptops:
            print(laptop.text)
            assert "Apple" in laptop.text, f"Title Apple is not found in {laptop.text}"


