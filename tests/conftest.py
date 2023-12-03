import pytest
from selenium.webdriver import Chrome


# fixture
@pytest.fixture(scope='session')
def simple_fixture_1():
    print('Це виконалося перед тестом')  # setup before test
    yield 1  # пeредає усправління в той тест тіло тесту або тіло функції
    print('Це виконалося AFTER тесту')  # setup after test)


@pytest.fixture(scope='class')  # if you specified this fixture it means in class we will run browser
def chrome(request):
    # service_object = Service("/Users/oleksandra/PycharmProjects/chromedriver_win32/chromedriver.exe")
    # driver_go = webdriver.Chrome(service=service_object)
    driver = Chrome()
    if request.cls:
        request.cls.driver = driver
    yield  # пeредає усправління в той тест тіло тесту або тіло функції
    driver.quit()  # setup after test)
