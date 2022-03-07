from asyncio import constants
from time import time
from src.pages.google import GooglePage


def test_caso1(browser):
  #Variables de la prueba
  TEXTO = "dresses"
  LISTA = "Price: Highest first"
  
  #Acceder a la página
  google_page = GooglePage(browser)

  #Validando que se muestre la página
  assert google_page.verify_display_sourche_input() == True

  #Escribir la entrada de texto
  google_page.write_search_input(TEXTO)

  #Validando que el texto que se esceribió sea correcto
  assert google_page.get_value_search_input() == TEXTO

  #Click al botón buscar
  google_page.click_button()

  #Verificar si el botón se muestra
  google_page.verify_display_button() == True

  #Acceder a la lista de categorías del producto
  google_page.select_dropdownlist(LISTA)

  #Verificar si se selecciona la categoría
  google_page.verify_display_list() == True
 