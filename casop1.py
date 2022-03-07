from lib2to3.pgen2 import driver
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(3)
  yield driver

  driver.quit()


def test_basic (browser):
  url=("https://www.google.com.do/")
  
  browser.get(url)

  elemento = browser.find_element_by_name("q")
  elemento.send_keys("Facebook")
  # driver.implicitly_wait(3)
  elemento.send_keys(Keys.ENTER)


