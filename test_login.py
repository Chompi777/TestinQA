from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Función para esperar y escribir en los campos del formulario
def escribir_campo(by, selector, valor):
    try:
        campo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, selector)))
        campo.clear()
        campo.send_keys(valor)
        print(f"✅ Se escribió '{valor}' en {selector}")
    except Exception as e:
        print(f"❌ No se encontró el campo {selector}: {e}")

try:
    # Ir a la página principal
    driver.get("https://ed.team/blog/las-mejores-apis-publicas-para-practicar")

    # Esperar y hacer clic en "Comienza gratis" para ir a registro
    wait = WebDriverWait(driver, 10)
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Comienza gratis')]")))
    boton.click()
    print("✅ Se hizo clic en 'Comienza gratis'")

    # Esperar que cargue la página de registro
    time.sleep(2)

    # Llenar los campos del formulario
    escribir_campo(By.ID, "name", "Salvador")
    escribir_campo(By.ID, "surname", "Guerra")
    escribir_campo(By.ID, "email", "germanfeo77@gmail.com")
    escribir_campo(By.ID, "password", "Morelia123")
    escribir_campo(By.ID, "confirmedPassword", "Morelia123")
    escribir_campo(By.ID, "city", "San Salvador")
    
    # Seleccionar el país "Argentina"
    select_country = wait.until(EC.element_to_be_clickable((By.ID, "country_name")))
    select_country.click()
    country = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Argentina')]")))
    country.click()
    print("✅ Se seleccionó 'Argentina' como país")

    # Marcar el checkbox de términos y condiciones
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, "accpet")))
    driver.execute_script("arguments[0].click();", checkbox)
    print("✅ Checkbox marcado")

    # Hacer clic en el botón de registro
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Regístrate ahora')]")))
    submit_button.click()
    print("✅ Se hizo clic en el botón de registro")

    time.sleep(3)  # Esperar que el registro sea completado

    # Parte 2: Ingreso con el usuario registrado
    # Ir a la página de login
    driver.get("https://app.ed.team/login")

    # Esperar que cargue la página de login
    escribir_campo(By.ID, "email", "stevepanameno@gmail.com")
    escribir_campo(By.ID, "password", "Morelia123")

    # Hacer clic en el botón de inicio de sesión
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'Iniciar sesión')]")))
    driver.execute_script("arguments[0].click();", login_button)
    print("✅ Se hizo clic en el botón de inicio de sesión")

    # Esperar la redirección
    time.sleep(3)  

    # Verificar si la URL final es la esperada
    if driver.current_url == "https://app.ed.team/":
        print("✅ Ingreso exitoso. Usuario autenticado correctamente en https://app.ed.team/")
    else:
        print(f"❌ No se redirigió correctamente. URL actual: {driver.current_url}")

except Exception as e:
    print(f"❌ Error general: {e}")

finally:
    driver.quit()
    print("🚀 Prueba finalizada")