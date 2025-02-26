from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Ir a la página principal
    driver.get("https://ed.team/blog/las-mejores-apis-publicas-para-practicar")

    # Esperar y hacer clic en "Comienza gratis" para ir a registro
    wait = WebDriverWait(driver, 10)
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Comienza gratis')]")))
    boton.click()
    print("✅ Se hizo clic en 'Comienza gratis'")

    # Esperar que cargue la página de registro
    time.sleep(2)  # Espera para asegurar que la página cargue completamente

    # Función para escribir en los campos del formulario
    def escribir_campo(by, selector, valor):
        try:
            campo = wait.until(EC.presence_of_element_located((by, selector)))
            campo.clear()
            campo.send_keys(valor)
            print(f"✅ Se escribió '{valor}' en {selector}")
        except Exception as e:
            print(f"❌ No se encontró el campo {selector}: {e}")

    # Llenar los campos del formulario con By.ID
    escribir_campo(By.ID, "name", "Salvador")
    escribir_campo(By.ID, "surname", "Guerra")
    escribir_campo(By.ID, "email", "stevepanameno@gmail.com")
    escribir_campo(By.ID, "password", "Morelia123")
    escribir_campo(By.ID, "confirmedPassword", "Morelia123")
    escribir_campo(By.ID, "city", "San Salvador")
    
    # Hacer clic en el select para desplegar la lista de países
    try:
        select_country = wait.until(EC.element_to_be_clickable((By.ID, "country_name")))
        select_country.click()
        print("✅ Se desplegó la lista de países")

        # Seleccionar el país "Argentina"
        country = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Argentina')]")))
        country.click()
        print("✅ Se seleccionó 'Argentina' como país")

    except Exception as e:
        print(f"❌ Error al seleccionar el país: {e}")

    # Marcar el checkbox de términos y condiciones
    try:
        checkbox = wait.until(EC.element_to_be_clickable((By.ID, "accpet")))
        driver.execute_script("arguments[0].click();", checkbox)
        print("✅ Checkbox marcado")
    except Exception as e:
        print(f"❌ Error al marcar el checkbox: {e}")

    # Hacer clic en el botón de registro
    try:
        # Ahora usamos el selector adecuado para el botón de "Registrarse ahora"
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Regístrate ahora')]")))
        submit_button.click()
        print("✅ Se hizo clic en el botón de registro")
    except Exception as e:
        print(f"❌ Error al hacer clic en el botón de registro: {e}")

    input("✅ Registro completado. Presiona ENTER para salir...")

except Exception as e:
    print(f"❌ Error general: {e}")

finally:
    driver.quit()
