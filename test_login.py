import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
#comando py -m pytest .\test_login.py -v
def test_login_exitoso():
    driver=webdriver.Chrome()#se trae para que se busque en la web

    try:
        driver.get("http://www.saucedemo.com/")#conduce a la pagina que se busca

        usuario=driver.find_element(By.ID,"user-name")#busca el id de esto
        password=driver.find_element(By.ID,"password")
        boton_login=driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()# si dio click

        assert "/inventory.html" in driver.current_url
        #validacion logo
        logo=driver.find_element(By.CLASS_NAME,"app_logo")
        assert logo.text=="Swag Labs"
        #validacion product
        titulo=driver.find_element(By.CSS_SELECTOR,"[data-test='title']")
        assert titulo.text=="Products"
    finally:
        driver.quit()

        