import pyautogui
import keyboard
import cv2

#Zoom da tela configurado em 100% - meia cheia


def main():
    while True:
        # Check if the "5" key is pressed
        if keyboard.is_pressed("num 5"):
            process_image("Images/Ocultar.png")
            process_image("Images/Ocultar2.png")
            print("Ocultar Perfil")

        # Check if the "8" key is pressed
        if keyboard.is_pressed("num 8"):
            process_image("Images/salvar.png")
            process_image("Images/salvar2.png")
            print("Salvar Perfil")

        # Check if the "4" key is pressed
        if keyboard.is_pressed("4"):
            process_image("Images/voltar.png")
            print("Voltar")
        
        # Check if the "6" key is pressed
        if keyboard.is_pressed("6"):
            process_image("Images/avancar.png")
            print("Avançar")

        # Check if the "7" key is pressed
        if keyboard.is_pressed("7"):
            process_image("Images/exibirMais.png")
            process_image("Images/exibirMais2.png")
            print("Exibir Mais")
        
        # Check if the "Up" key is pressed
        if keyboard.is_pressed("+"):
            pyautogui.scroll(700)
            print("Page Up")

        # Check if the "Down" key is pressed
        if keyboard.is_pressed("-"):
            pyautogui.scroll(-700)
            print("Page Down")

def process_image(image_path):
    # Convert the string to an OpenCV numpy array
    image = cv2.imread(image_path)

    # Locate the image on the screen
    coordinates = pyautogui.locateOnScreen(image, confidence=0.8)

    # If the image was found, click on it
    if coordinates:
        pyautogui.click(coordinates)

if __name__ == "__main__":
    main()

