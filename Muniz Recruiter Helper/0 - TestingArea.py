from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import keyboard  # Importa a biblioteca keyboard

# Mapeamento de teclas para os botões
KEY_MAPPING = {
    "save": "s",
    "hide": "h",
    "previous": "p",
    "next": "n"
}

# Inicializa o serviço do ChromeDriver
chromedriver_path = r'C:\Users\Paulo\OneDrive\Documentos\Hackerlife\VSCode\Muniz Recruiter Helper\chromedriver.exe'
service = ChromeService(executable_path=chromedriver_path)

# Inicializa o navegador Chrome sem abrir uma nova janela/aba
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")  # Conecta ao navegador aberto

driver = webdriver.Chrome(service=service, options=options)

try:
    # Pega a alça (handle) da janela atual
    current_window = driver.current_window_handle

    # Entra no loop para verificar a página ativa
    while True:
        # Muda para a janela atual
        driver.switch_to.window(current_window)

        # Espera pelas teclas pressionadas
        key_pressed = keyboard.read_event(suppress=True).name

        if key_pressed in KEY_MAPPING.values():
            if key_pressed == KEY_MAPPING["save"]:
                # Encontra e clica no botão "Save to pipeline"
                save_button = driver.find_element_by_css_selector(".save-to-pipeline__button")
                save_button.click()
            elif key_pressed == KEY_MAPPING["hide"]:
                # Encontra e clica no botão "Hide"
                hide_button = driver.find_element(By.XPATH, "//span[contains(., 'Hide')]/ancestor::button")
                hide_button.click()
            elif key_pressed == KEY_MAPPING["previous"]:
                # Encontra e clica no botão "Previous"
                previous_button = driver.find_element(By.CSS_SELECTOR, "button.skyline-pagination-button[disabled]")
                previous_button.click()
            elif key_pressed == KEY_MAPPING["next"]:
                # Encontra e clica no botão "Next"
                next_button = driver.find_element(By.CSS_SELECTOR, "a.skyline-pagination-link[rel='next']")
                next_button.click()

finally:
    # Encerra o navegador ao dar o comando Quit
    driver.quit()
