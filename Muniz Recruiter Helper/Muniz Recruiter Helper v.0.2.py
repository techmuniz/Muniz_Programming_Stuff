import cv2
import pyautogui
import keyboard

def main():
    image_path = "Images/Ocultar.png"

    # Convert the string to an OpenCV numpy array
    image = cv2.imread(image_path)

    while True:
        # Check if the "End" key is pressed
        if keyboard.is_pressed("End"):
            # Locate the image on the screen
            coordinates = pyautogui.locateOnScreen(image, confidence=0.8)

            # If the image was found, click on it
            if coordinates:
                pyautogui.click(coordinates)

if __name__ == "__main__":
    main()