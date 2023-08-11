import pyautogui
import keyboard
import cv2

#Zoom da tela configurado em 90% - meia tela


def main():
    while True:
        # Check if the "End" key is pressed
        if keyboard.is_pressed("End"):
            process_image("Images/Ocultar.png")

        # Check if the "Delete" key is pressed
        if keyboard.is_pressed("Delete"):
            process_image("Images/salvar.png")

        # Check if the "Insert" key is pressed
        if keyboard.is_pressed("Insert"):
            process_image("Images/voltar.png")
        
        # Check if the "Home" key is pressed
        if keyboard.is_pressed("Home"):
            process_image("Images/avancar.png")

        # Check if the "printScreen" key is pressed
        if keyboard.is_pressed("print_screen"):
            process_image("Images/exibirMais.png")
        
        # Check if the "Page Up" key is pressed
        if keyboard.is_pressed("Page Up"):
            pyautogui.scroll(700)

        # Check if the "Page Down" key is pressed
        if keyboard.is_pressed("Page Down"):
            pyautogui.scroll(-700)

def process_image(image_path):
    # Convert the string to an OpenCV numpy array
    image = cv2.imread(image_path)

    # Locate the image on the screen
    coordinates = pyautogui.locateOnScreen(image, confidence=0.9)

    # If the image was found, click on it
    if coordinates:
        pyautogui.click(coordinates)

if __name__ == "__main__":
    main()