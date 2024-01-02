import time
from Home_work_10_rozetka.Main_rozetka_page.Rozetka_laptops_page import Laptop_page


class TestLaptopPage:

    def test_count_per_page(self, chrome):
        target_count = 60
        page = Laptop_page(chrome)
        page.open()
        count_per_page = page.get_count_per_page(target_count)
        assert target_count == count_per_page, "Target is NOT equal to items per page"

    def test_scroll_down_to_element(self, chrome):
        page = Laptop_page(chrome)
        page.open()
        page.scroll_down_to_element(page.pagination_1) #if no property page pagination is like method you can't take webelement methods
        assert page.pagination_1.is_enabled(), "Pagination 1 is not enabled"
        assert page.is_previous_btn_disabled(), "Previous button is NOT disabled"
        assert page.is_next_button_enabled(), "Next button is not enabled"

    def test_scroll_down_and_click_on_next(self, chrome):
        target_count_page2 = 60
        page = Laptop_page(chrome)
        page.open()
        page.scroll_down_to_element(page.next_button)
        time.sleep(2)
        page.next_button.click()
        count_per_page = page.get_count_per_page(target_count_page2)
        assert target_count_page2 == count_per_page, "Target is NOT equal to items per page"
        assert page.pagination_2.is_selected(), "Pagination 2 is not selected"
        assert 'page=2' in page.URL, "Title doesn't contain page 2 "

