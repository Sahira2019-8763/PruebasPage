

from asyncio import constants
from time import time
from src.pages.google import GooglePage


def test_caso1(browser):
  TEXTO = "dresses"
  LISTA = "Price: Highest first"
  google_page = GooglePage(browser)
  assert google_page.verify_display_sourche_input() == True
  google_page.write_search_input(TEXTO)
  assert google_page.get_value_search_input() == TEXTO
  google_page.click_button()
  google_page.verify_display_button() == True
  google_page.select_dropdownlist(LISTA)
  google_page.verify_display_list() == True
 



 