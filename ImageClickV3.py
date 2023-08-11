import cv2
import pyautogui
import keyboard

def main():
    image_path_ocultar = "Images/Ocultar.png"
    image_path_salvar = "Images/salvar.png"

    while True:
        # Check if the "End" key is pressed
        if keyboard.is_pressed("End"):
            process_image(image_path_ocultar)

        # Check if the "Delete" key is pressed
        if keyboard.is_pressed("Delete"):
            process_image(image_path_salvar)

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