from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class PageDatePicker:
    URL = 'https://demoqa.com/date-picker'
    MONTHS = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }
    locator_button_previous = (By.XPATH, '//button[contains(@class,"previous")]')
    locator_button_next = (By.XPATH, '//button[contains(@class,"next")]')

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.select_date_locator = (By.ID, 'datePickerMonthYearInput')

    def open(self):
        self.__driver.get(self.URL)
        return self

    def set_date_directly(self, selected_date):
        ''' param selected date format == 12/18/2023 where 12 is month, 18 is day and 2023 is year it's string'''
        date_input = self.__driver.find_element(*self.select_date_locator)
        # date_input.clear()
        date_input.send_keys(Keys.CONTROL + 'A')
        date_input.send_keys(Keys.DELETE)
        date_input.send_keys(selected_date)
        date_input.send_keys(Keys.ENTER)
        pass

    def set_date_by_picker(self, selected_date):
        ''' param selected date format == 12/18/2023 where 12 is month, 18 is day and 2023 is year it's string'''
        # date_input = self.driver.find_element(*self.select_date_input)
        month = selected_date.split('/')[0]
        try:
            month = int(month)
        except ValueError:
            month = month

        day = selected_date.split('/')[1]
        year = selected_date.split('/')[2]
        self.__set_date_by_picker(month=month, day=day, year=year)

    def __set_date_by_picker(self, month: int, day: int, year: int):
        self.__set_month(month=month)
        self.__set_year(year=year)


    def open_date_picker(self):  # return WebElement
        element = self.__driver.find_element(*self.select_date_locator)
        element.click()
        return element

    def __set_month(self, month: int | str):
        locator = '//select[contains(@class,"month-select")]'
        element = self.__driver.find_element(By.XPATH, locator)

        select = Select(element)
        if type(month) is int:
            select.select_by_index(month)
            # select.select_by_value(month)
        elif type(month) is str:
            select.select_by_visible_text(month)
        else:
            raise TypeError(f'Month type should be int or str, was given {type(month)}')

    def __set_year(self, year: int):
        locator = '//select[contains(@class,"year-select")]'
        element = self.__driver.find_element(By.XPATH, locator)
        select = Select(element)
        select.select_by_value(year)


    def get_current_date(self):
        locator = '//div[contains(@class,"day--today")]' #finding only a day
        element = self.__driver.find_element(By.XPATH, locator)
        aria_label_attribute = element.get_attribute('aria-label')
        current_date = aria_label_attribute.split(' ', 2)[2]
        return current_date

    def scroll_to_target_year(self,target_year: int):
        locator_button_previous = (By.XPATH, '//button[contains(@class,"previous")]')
        locator_button_next = (By.XPATH, '//button[contains(@class,"next")]')
        previous_button = self.__driver.find_element(*locator_button_previous)
        next_button = self.__driver.find_element(*locator_button_next)
        current_year_in_picker_locator = (By.XPATH,'//div[@class="react-datepicker__header"]/div[contains(@class,"current")]')
        current_year = int(self.__driver.find_element(*current_year_in_picker_locator).text.split(' ')[1])
        if target_year > self.get_current_year():
            while target_year > self.get_current_year():
                next_button.click()
        elif target_year < self.get_current_year():
            while target_year < self.get_current_year():
                    previous_button.click()
            else:
                pass

    def click_on_next_prev_btn(self, direction, count):
        previous_button = self.__driver.find_element(*self.locator_button_previous)
        next_button = self.__driver.find_element(*self.locator_button_next)

        if direction == 'next':
            for _ in range(count):
                next_button.click()
        elif direction == 'previous':
            for _ in range(count):
                previous_button.click()
        else:
            print("Direction is invalid")


    def scroll_to_target_month_within_year(self, target_date):
        target_year = int(target_date.split('/')[-1])
        target_month = int(target_date.split('/')[0])
        current_month_in_picker_locator = (By.XPATH, '//div[@class="react-datepicker__header"]/div[contains(@class,"current-month")]')
        self.scroll_to_target_year(target_year)
        current_month = self.__driver.find_element(*current_month_in_picker_locator).text.split(' ')[0]
        print("Scrolling from month:", current_month)
        if target_month > self.MONTHS[current_month]:
            count = target_month - self.MONTHS[current_month]
            self.click_on_next_prev_btn(direction='next', count=count)
        elif target_month < self.MONTHS[current_month]:
            count = self.MONTHS[current_month] - target_month
            self.click_on_next_prev_btn(direction='previous', count=count)
        else:
            print("Can't scroll through months")
        current_month = self.__driver.find_element(*current_month_in_picker_locator).text.split(' ')[0]
        print("Month to which we scrolled:", current_month)




    def get_current_year(self):
        current_year_in_picker_locator = (By.XPATH, '//div[@class="react-datepicker__header"]/div[contains(@class,"current")]')
        current_year = int(self.__driver.find_element(*current_year_in_picker_locator).text.split(' ')[1])
        return current_year

    def get_current_month_within_current_year(self):
        current_month_in_picker_locator = '//div[@class="react-datepicker__header"]/div[contains(@class,"current-month")]'
        # current_month_within_current_year = self.__driver.find_element(current_month_in_picker_locator).text.split(' ')[0])
        if self.get_current_year() in range(1900, 2127):
            current_month_within_current_year = self.__driver.find_element(By.XPATH, current_month_in_picker_locator)
            current_month_text = current_month_within_current_year.text.split(' ')[0]
        else:
            print('Year is not in accepted range')
        return current_month_text
