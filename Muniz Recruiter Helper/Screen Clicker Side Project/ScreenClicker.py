import keyboard
import pyautogui

def execute_macro_next():
    # Coloque aqui as coordenadas da região que você quer clicar
    x, y = 1840,162

    # Clica na posição especificada
    pyautogui.click(x, y)

def execute_macro_previous():
    # Coloque aqui as coordenadas da região que você quer clicar
    x, y = 1635,162

    # Clica na posição especificada
    pyautogui.click(x, y)

# Função a ser chamada quando a tecla F4 for pressionada
def on_f4_press(e):
    execute_macro_next()

def on_f3_press(e):
    execute_macro_previous()

# Associa a função ao pressionamento da tecla F4
keyboard.on_press_key("F4", on_f4_press)
keyboard.on_press_key("F3", on_f3_press)

# Mantém o script em execução
keyboard.wait("esc")





# 1840,162 -- Next candidate
# 1635,162 -- Previous candidate
