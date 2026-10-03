import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#comando py -m pytest .\test_login.py -v
def test_cart():
    driver=webdriver.Chrome()#se trae para que se busque en la web
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://www.saucedemo.com/")#conduce a la pagina que se busca
        usuario = wait.until( EC.visibility_of_element_located((By.ID, "user-name")) )

        usuario=driver.find_element(By.ID,"user-name")#busca el id de esto
        password=driver.find_element(By.ID,"password")
        boton_login=driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()# si dio click
        wait.until(EC.url_contains("/inventory.html"))

        # Verificar título "Products"
        titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']") )
)
        assert titulo.text == "Products"


        # Verificar que existan productos
        productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        assert len(productos) > 0

        # Obtener el primer producto
        primer_producto = productos[0]

        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        print("Primer producto:", nombre_producto)
        print("Precio:", precio_producto)


  
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")

        # Espera a que el botón este disponible para hacer click
        wait.until(EC.element_to_be_clickable(boton_agregar))

        boton_agregar.click()

        # Espera que aparezca el contador del carrito
        contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

        assert contador_carrito.text == "1"


        # Hacer click en el carrito
        carrito = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))

        carrito.click()

        wait.until(EC.url_contains("/cart.html"))


        producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

        assert producto_carrito.text == nombre_producto

        print("Producto agregado correctamente:", producto_carrito.text)

    finally:
        driver.quit()
