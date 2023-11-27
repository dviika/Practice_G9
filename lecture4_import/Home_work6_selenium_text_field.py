from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

service_object = Service("/Users/oleksandra/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver: object = webdriver.Chrome(service=service_object)
driver.get("https://demoqa.com/text-box")
# driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)

fullName = driver.find_element(By.XPATH, "//input[@id ='userName']")# why I can do it in one line ? send_keys('Oleksandra Kalinichenko')
fullName.send_keys('Oleksandra Kalinichenko')
fullName_text = fullName.get_attribute('value')
# print(fullName_text)
email = driver.find_element(By.XPATH, "//input[@id ='userEmail']")
email.send_keys('O.Kalinichenko@gmail.com')
email_text = email.get_attribute('value')
currentAddress = driver.find_element(By.XPATH, "//textarea[@id ='currentAddress']")
currentAddress.send_keys('Gogol street 57, Kyiv, 04050')
currentAddress_text = currentAddress.get_attribute('value')
permanentAddress = driver.find_element(By.XPATH, "//textarea[@id ='permanentAddress']")
permanentAddress.send_keys('Prorizna street 57, Kyiv, 00050')
permanentAddress_text = permanentAddress.get_attribute('value')
submit = driver.find_element(By.XPATH, "//button[@id ='submit']").click()

assert fullName_text == 'Oleksandra Kalinichenko'
assert email_text == 'O.Kalinichenko@gmail.com'
assert currentAddress_text == 'Gogol street 57, Kyiv, 04050'
assert permanentAddress_text == 'Prorizna street 57, Kyiv, 00050'
driver.quit()