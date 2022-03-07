from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("http://automationpractice.com/index.php")
  driver.implicitly_wait(7)
  driver.maximize_window() 
  driver.implicitly_wait(5)
  yield driver
  driver.quit()
