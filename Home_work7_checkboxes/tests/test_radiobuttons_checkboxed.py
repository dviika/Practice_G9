import pytest
from Home_work7_checkboxes.helper.checkbox_logic import radio_button, radio_button_label, selected_name, selected_text, \
    generate_dictionary_of_radio_but_statuses
@pytest.mark.usefixtures('chrome')
class TestRadioButtons:

    def test_select_radio_button_yes(self):
        NAME = "Yes"
        self.driver.get('https://demoqa.com/radio-button')
        element_radio_button = radio_button(driver=self.driver, name=NAME) # finding an element and reurn instance of the element
        element_radio_button_label = radio_button_label(driver=self.driver, name=NAME)
        assert element_radio_button_label.is_displayed(), "Radio button is not displayed"

        if not element_radio_button.is_selected():
            element_radio_button_label.click()
        generate_dictionary_of_radio_but_statuses(driver=self.driver)

        assert element_radio_button.is_selected(), "Radio button is not selected"

        element_selected_text = selected_text(driver=self.driver)
        assert element_selected_text.is_displayed(), "'You have selected' text is not displayed"

        element_selected_name = selected_name(driver=self.driver, name=NAME)
        assert element_selected_name.text == NAME, f"Selected radio button is incorrect {NAME}"

    def test_select_button_impressive(self):
        NAME ='Impressive'
        self.driver.get('https://demoqa.com/radio-button')
        element_radio_button = radio_button(driver=self.driver,
                                            name=NAME)  # finding an element and reurn instance of the element
        element_radio_button_label = radio_button_label(driver=self.driver, name=NAME)
        assert element_radio_button_label.is_displayed(), "Radio button is not displayed"

        if not element_radio_button.is_selected():
            element_radio_button_label.click()
        generate_dictionary_of_radio_but_statuses(driver=self.driver)

        assert element_radio_button.is_selected(), "Radio button is not selected"

        element_selected_text = selected_text(driver=self.driver)
        assert element_selected_text.is_displayed(), "'You have selected' text is not displayed"

        element_selected_name = selected_name(driver=self.driver, name=NAME)
        assert element_selected_name.text == NAME, f"Selected radio button is incorrect {NAME}"

    def test_select_button_no(self):
        NAME = 'No'
        self.driver.get('https://demoqa.com/radio-button')
        element_radio_button = radio_button(driver=self.driver,
                                            name=NAME)  # finding an element and reurn instance of the element
        element_radio_button_label = radio_button_label(driver=self.driver, name=NAME)
        assert element_radio_button_label.is_displayed(), "Radio button is not displayed"

        if not element_radio_button.is_enabled():
            self.driver.execute_script('arguments[0].removeAttribute("disabled");', element_radio_button)
        element_radio_button_label.click()
        generate_dictionary_of_radio_but_statuses(driver=self.driver)

        assert element_radio_button.is_selected(), "Radio button is not selected"