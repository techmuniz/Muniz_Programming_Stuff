import pyautogui
import keyboard
import cv2

def get_user_keys():
    # Colete a entrada do usuário para cada tecla e retorne em um dicionário
    keys = {
        "ocultar": input("Tecla para 'Ocultar Perfil': "),
        "salvar": input("Tecla para 'Salvar Perfil': "),
        "voltar": input("Tecla para 'Voltar': "),
        "avancar": input("Tecla para 'Avançar': "),
        "exibir_mais": input("Tecla para 'Exibir Mais': "),
        "page_up": input("Tecla para 'Page Up': "),
        "page_down": input("Tecla para 'Page Down': ")
    }
    return keys

def main():
    user_keys = get_user_keys()

    while True:
        # Check each action based on user-defined keys
        if keyboard.is_pressed(user_keys["ocultar"]):
            process_image("Images/Ocultar.png")
            process_image("Images/Ocultar2.png")
            print("Ocultar Perfil")

        if keyboard.is_pressed(user_keys["salvar"]):
            process_image("Images/salvar.png")
            process_image("Images/salvar2.png")
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
        
        if keyboard.is_pressed(user_keys["page_up"]):
            pyautogui.scroll(700)
            print("Page Up")

        if keyboard.is_pressed(user_keys["page_down"]):
            pyautogui.scroll(-700)
            print("Page Down")

def process_image(image_path):
    image = cv2.imread(image_path)
    coordinates = pyautogui.locateOnScreen(image, confidence=0.8)
    if coordinates:
        pyautogui.click(coordinates)

if __name__ == "__main__":
    main()
