import pytest
from Home_work7_checkboxes.helper.checkbox_logic import select_radio_button, generate_dictionary_of_radio_but_statuses


@pytest.mark.usefixtures('chrome')
class TestRadioButtons:

    def test_select_button_yes(self):
        self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(driver=self.driver, name='Yes')

    def test_select_button_impressive(self):
        self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(driver=self.driver, name='Impressive')

    def test_select_button_no(self):
        self.driver.get('https://demoqa.com/radio-button')
        select_radio_button(driver=self.driver, name='No')

    def test_get_radio_button_statuses(self):
        self.driver.get('https://demoqa.com/radio-button')
        generate_dictionary_of_radio_but_statuses(driver=self.driver)
