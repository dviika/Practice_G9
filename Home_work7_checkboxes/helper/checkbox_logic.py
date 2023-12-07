from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def radio_button(driver: WebDriver, name: str):  # acept chrome driver and name
    locator = f'//label[text()="{name}"]//ancestor::div[contains(@class, "radio")]/input'
    element_radio_button = driver.find_element(By.XPATH, locator)
    return element_radio_button


def radio_button_label(driver: WebDriver, name: str):
    locator = f'//label[text()="{name}"]//ancestor::div[contains(@class, "radio")]/label'
    element_label = driver.find_element(By.XPATH, locator)
    return element_label


def selected_text(driver: WebDriver):
    locator_selected_text = '//p[@class="mt-3"]'
    element_selected_text = driver.find_element(By.XPATH, locator_selected_text)
    return element_selected_text


def selected_name(driver: WebDriver, name: str):
    locator_selected_name = f'//span[@class="text-success" and text() = "{name}"]'
    element_selected_name = driver.find_element(By.XPATH, locator_selected_name)
    return element_selected_name


def generate_dictionary_of_radio_but_statuses(driver: WebDriver):
    dict = {}
    locator = '//div[contains(@class, "radio")]'  # finding all 3 radiobuttons
    list_of_radio = driver.find_elements(By.XPATH, locator)
    assert list_of_radio, "Elements are not found"
    for div in list_of_radio:
        radio_but_name = div.text
        radio_button_locator = f'//label[text()="{radio_but_name}"]//ancestor::div[contains(@class, "radio")]/input'
        radio_but = driver.find_element(By.XPATH, radio_button_locator)
        radio_button_enabled = radio_but.is_enabled()
        radio_button_selected = radio_but.is_selected()
        dict[radio_but_name] = {'enabled': radio_button_enabled, 'selected': radio_button_selected}

    print(dict)
