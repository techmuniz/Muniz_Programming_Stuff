import keyboard
import pyautogui
import time

def execute_macro_next():
    # Coloque aqui as coordenadas da região que você quer clicar
    x, y = 1635, 162

    # Clica na posição especificada
    pyautogui.click(x, y)

def execute_macro_previous():
    # Coloque aqui as coordenadas da região que você quer clicar
    x, y = 1840, 162

    # Clica na posição especificada
    pyautogui.click(x, y)

def execute_macro_del():
    # Coloque aqui as coordenadas da região que você quer clicar
    x, y = 457, 572

    # Clica na posição especificada
    pyautogui.click(x, y)

def execute_macro_end():
    # Clica na primeira palavra "Ocultar" da tela
    pyautogui.click(pyautogui.locateCenterOnScreen("Ocultar"))

# Função a ser chamada quando a tecla Insert for pressionada
def on_insert_press(e):
    execute_macro_next()

# Função a ser chamada quando a tecla Home for pressionada
def on_home_press(e):
    execute_macro_previous()

# Função a ser chamada quando a tecla Del for pressionada
def on_del_press(e):
    execute_macro_del()

# Função a ser chamada quando a tecla End for pressionada
def on_end_press(e):
    pyautogui.click(pyautogui.locateCenterOnScreen("Ocultar"))

# Adiciona uma nova função para a tecla Page Down
def on_page_down_press(e):
    pyautogui.scroll(-1300)

# Adiciona uma nova função para a tecla Page Up
def on_page_up_press(e):
    pyautogui.scroll(1300)

# Associa as funções aos pressionamentos das teclas
keyboard.on_press_key("insert", on_insert_press)
keyboard.on_press_key("home", on_home_press)
keyboard.on_press_key("delete", on_del_press)
keyboard.on_press_key("end", on_end_press)
keyboard.on_press_key("page down", on_page_down_press)
keyboard.on_press_key("page up", on_page_up_press)

# Mantém o script em execução
keyboard.wait("esc")
