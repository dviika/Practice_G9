import pytest, time
import pytest as mytest #
from datetime import date
from selenium.webdriver.support import expected as EC
from lecture4_import.test_sour

#alt+ enter
from repo1.Practice_G9.lecture4_import.test_source.import_data import NAME


#decorator for understanding that it's a test
@pytest.fixture()
def my_fixture_name():
    time.sleep(2)
    c1 = EC.visibility_of_element_located()

print(NAME)