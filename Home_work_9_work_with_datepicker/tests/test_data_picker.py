from Home_work_9_work_with_datepicker.Page_DatePicker.page_dataPicker import PageDatePicker


class TestDatePicker:

    def test_select_date(self, chrome):
        target_date = '12//28/2023'
        page = PageDatePicker(chrome)
        page.open()
        page.open_date_picker()

        # page.set_date_by_picker('3/18/2023')  # April
        # # page.set_date_by_picker('0/18/2023')
        # page.set_date_by_picker('October/18/2023')

    def test_current_date(self, chrome):
        page = PageDatePicker(chrome)
        page.open()
        page.open_date_picker()
        print(page.get_current_date())

    def test_scroll_to_target_date(self, chrome):
        target_date = '11/28/2020'
        page = PageDatePicker(chrome)
        page.open()
        page.open_date_picker()
        
        target_year = int(target_date.split('/')[-1])
        page.scroll_to_target_year(target_year)
        print(page.get_current_month_within_current_year())
