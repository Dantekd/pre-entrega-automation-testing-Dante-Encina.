import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
#comando py -m pytest .\test_login.py -v
def test_inventory_exitoso():
    driver=webdriver.Chrome()#se trae para que se busque en la web

    try:
        driver.get("http://www.saucedemo.com/")#conduce a la pagina que se busca

        usuario=driver.find_element(By.ID,"user-name")#busca el id de esto
        password=driver.find_element(By.ID,"password")
        boton_login=driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()# si dio click

        assert driver.title =="Swag Labs"

        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(productos)>0
        primer_producto =productos[0]
        nombre_producto=primer_producto.find_element(By.CLASS_NAME,"inventory_item_name").text
        precio_producto=primer_producto.find_element(By.CLASS_NAME,"inventory_item_price").text

        assert nombre_producto =="Sauce Labs Backpack"
        assert precio_producto=="$29.99"
        #verifica menu
        menu=driver.find_element(By.ID,"react-burger-menu-btn")

        assert menu.is_displayed()
        #verifica filtro
        filtro=driver.find_element(By.CLASS_NAME,"product_sort_container")
        
        assert filtro.is_displayed()
    finally:
        driver.quit()