from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Ir a la página
    driver.get("https://ed.team/blog/las-mejores-apis-publicas-para-practicar")

    # Esperar a que el botón sea clickeable
    wait = WebDriverWait(driver, 10)
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Comienza gratis')]")))

    # Hacer clic en el botón
    boton.click()

    # Esperar para ver el resultado antes de cerrar
    input("Presiona ENTER para cerrar...")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
