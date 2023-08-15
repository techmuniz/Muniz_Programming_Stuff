import cv2
import pyautogui

image_path = "Images/Ocultar.png"

# Convert the string to an OpenCV numpy array
image = cv2.imread(image_path)

# Locate the image on the screen
coordinates = pyautogui.locateOnScreen(image, confidence=0.5)

# If the image was found, click on it
if coordinates:
    pyautogui.click(coordinates)
