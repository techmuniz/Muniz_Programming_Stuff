import pyautogui
import keyboard
import cv2
import time

def get_user_keys():
    # Colete a entrada do usuário para cada tecla e retorne em um dicionário
    keys = {
        "ocultar": input("Tecla para 'Ocultar Perfil': "),
        "salvar": input("Tecla para 'Salvar Perfil': "),
        "voltar": input("Tecla para 'Voltar': "),
        "avancar": input("Tecla para 'Avançar': "),
        "exibir_mais": input("Tecla para 'Exibir Mais': "),
    }
    return keys

def main():
    user_keys = get_user_keys()

    while True:
        # Check each action based on user-defined keys
        if keyboard.is_pressed(user_keys["ocultar"]):
            pyautogui.scroll(4000)
            time.sleep(0.5)    
            pyautogui.scroll(4000)
            time.sleep(0.5)                    
            process_image("Images/Ocultar.png")
            process_image("Images/Ocultar2.png")
            time.sleep(0.5)            
            process_image("Images/avancar.png")    
            print("Ocultar Perfil")

        if keyboard.is_pressed(user_keys["salvar"]):
            pyautogui.scroll(4000)
            time.sleep(0.5)    
            pyautogui.scroll(4000)
            time.sleep(0.5)                    
            process_image("Images/salvar.png")
            process_image("Images/salvar2.png")
            process_image("Images/avancar.png")    
            print("Salvar Perfil")

        if keyboard.is_pressed(user_keys["voltar"]):
            process_image("Images/voltar.png")      
            print("Voltar")
        
        if keyboard.is_pressed(user_keys["avancar"]):
            process_image("Images/avancar.png")
            print("Avançar")

        if keyboard.is_pressed(user_keys["exibir_mais"]):
            process_image("Images/exibirMais.png")
            process_image("Images/exibirMais2.png")
            print("Exibir Mais")

        # Check if the "0" key is pressed to edit keys
        if keyboard.is_pressed("0"):
            print("\nEditando teclas:")
            user_keys = get_user_keys()  # Solicitar novas teclas ao usuário

def process_image(image_path):
    image = cv2.imread(image_path)
    coordinates = pyautogui.locateOnScreen(image, confidence=0.8)
    if coordinates:
        pyautogui.click(coordinates)

if __name__ == "__main__":
    main()
