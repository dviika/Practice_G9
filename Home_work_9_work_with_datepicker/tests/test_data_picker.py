from home_work_9_work_with_datepicker.pageDatePicker import pageDataPicker

class testDatePicker:

    def test_select_date(self, chrome):
        target_date = '12//28/2023'
        page = PageDatePicker(chrome)
        page.open()
        page.open_date_picker()

        # page.set_date_by_picker('3/18/2023')  # April
        # # page.set_date_by_picker('0/18/2023')
        # page.set_date_by_picker('October/18/2023')

    def test_current_date(self, chrome):
        page = pageDataPicker(chrome)
        page.open()
        page.open_date_picker()
        print(page.get_current_date())

    def test_scroll_to_target_date(self, chrome):
        target_date = '11/28/2020'
        page = pageDataPicker(chrome)
        page.open()
        page.open_date_picker()
        target_year = int(target_date.split('/')[-1])
        page.scroll_to_target_year(target_year)
        print(page.get_current_month_within_current_year())

    def test_scroll_to_month(self, chrome):
        target_date = '4/5/2019'
        page = pageDataPicker(chrome)
        page.open()
        page.open_date_picker()
        page.scroll_to_target_month_within_year(target_date)

