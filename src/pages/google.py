from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class GooglePage:
    def __init__(self, browser):
        self.browser = browser

    @classmethod
    def campo_input(cls):
    
        return(By.XPATH, "//input[@class='search_query form-control ac_input']")
    
    @classmethod
    def btn(cls):
    
        return(By.NAME, "submit_search")

    @classmethod
    def dropdownlist(cls):
    
        return(By.ID, "selectProductSort")
    




    def write_search_input(self, texto):
        elemento = self.browser.find_element(*self.campo_input())
        elemento.send_keys(texto)
        

    def get_value_search_input(self):
        elemento = self.browser.find_element(*self.campo_input())
        return elemento.get_attribute("value")
        
    def verify_display_sourche_input(self):
        elemento = self.browser.find_element(*self.campo_input())
        return elemento.is_displayed()

    def click_button(self):
        elemento = self.browser.find_element(*self.btn())
        elemento.click()

    def verify_display_button(self):
        elemento = self.browser.find_element(*self.btn())
        return elemento.is_displayed()
    
    def select_dropdownlist(self, value):
        elemento = self.browser.find_element(*self.dropdownlist())
        select = Select(elemento)
        select.select_by_visible_text(value)


    
    def verify_display_list(self):
        elemento = self.browser.find_element(*self.dropdownlist())
        return elemento.is_displayed()
    
        




