"""
Main goal: Auto-discard candidates in pre-shortlist stage [Matching]

Steps:
    [   ] 1: Scroll down
    [   ] 2: Locate "Discard" button
    [   ] 3: Click "Discard" button
    [   ] 4: Locate "Missing Technical Skills" option 
        [   ] 4.1 Here, we can implement other options, including adding a message in Additional comments)
    [   ] 5: Locate "Submit" button
    [   ] 6: Click "Submit" button
    [   ] 7: Wait command
        [   ] 7.1 - Start with 2 seconds
    [   ] 8. Click on next candidate [Optional]
        [   ] 8.1 I don't know how to scale this to other computers, as the clicking in the screen would be personalized for my screen
    [   ] 9. Create a UI
        [   ] 9.1 - Button for Discarding candidate        
    
"""
import time
import keyboard
import pyautogui
import cv2
import numpy as np

# Função para localizar um elemento na tela usando uma imagem de referência
def locate_element(image_path, confidence_threshold=0.4):
    screen_width, screen_height = pyautogui.size()
    screenshot = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
    screenshot = np.array(screenshot)
    template = cv2.imread(image_path)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence_threshold:
        x, y, w, h = (*max_loc, *template.shape[1::-1])
        center_x = x + w // 2
        center_y = y + h // 2
        return center_x, center_y


    return None

# Função para clicar em um ponto na tela
def click_at(x, y):
    pyautogui.click(x, y)

# Função para rolar a tela para baixo usando o scroll do mouse
def scroll_down():
    pyautogui.scroll(4000)
    time.sleep(0.5)
    pyautogui.scroll(4000)
    time.sleep(0.5)

# Função para esperar por alguns segundos
def wait(seconds):
    time.sleep(seconds)

# Ask the user to input a key to start the script
start_key = input("Press the desired key to start the script: ")

while True:

    # Wait for the user to press the specified key to start
    print(f"Press '{start_key}' to start the script...")
    keyboard.wait(start_key)
    print("Starting the script!")

    # Etapa 1: Rolar para baixo
    wait(1)
    scroll_down()

    # Etapa 2: Localizar o botão "Discard"
    discard_button_location = locate_element('Matching clicker/Img/discard_button.png')
    if discard_button_location:
        # Etapa 3: Clicar no botão "Discard"
        click_at(*discard_button_location)
        print('Clicking Discard Button')
        wait(1)

        # Etapa 4: Localizar a opção "Missing Technical Skills"
        missing_skills_location = locate_element('Matching clicker/Img/missing_skills_option.png')
        if missing_skills_location:
            click_at(*missing_skills_location)
            print('Clicking Missing skills Button')
            wait(1)

            # Etapa 5: Localizar o botão "Submit"
            submit_button_location = locate_element('Matching clicker/Img/submit_button.png')
            if submit_button_location:
                # Etapa 6: Clicar no botão "Submit"
                click_at(*submit_button_location)
                print('Clicking Submit Button')
                wait(6)

                click_at(1962, 871)

            else:
                print("Botão 'Submit' não encontrado.")
        else:
            print("Opção 'Missing Technical Skills' não encontrada.")
    else:
        print("Botão 'Discard' não encontrado.")






                # 
# 749, 839