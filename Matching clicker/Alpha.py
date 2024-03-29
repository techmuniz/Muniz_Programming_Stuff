import time
import keyboard
import pyautogui
import cv2
import numpy as np

# Função para localizar um elemento na tela usando uma imagem de referência
def locate_element(image_path, confidence_threshold=0.35):
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

# Ask the user to input the keys to start the script
start_key = input("Press the first assigned key to start the script: ")
second_key = input("Press the second assigned key to perform the alternate action: ")

while True:
    # Wait for the user to press the specified key to start
    print(f"Press '{start_key}' to start the script or '{second_key}' to perform alternate action...")
    pressed_key = keyboard.read_event(suppress=True).name
    if pressed_key == start_key:
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
            wait(0.5)

            # Etapa 4: Localizar a opção "Missing Technical Skills"
            missing_skills_location = locate_element('Matching clicker/Img/missing_skills_option.png')
            if missing_skills_location:
                click_at(*missing_skills_location)
                print('Clicking Missing skills Button')
                wait(1)

                # Etapa 5: Localizar o botão "Submit"
                submit_button_location = locate_element('Matching clicker/Img/submit_button.png')
                if submit_button_location:
                    click_at(*submit_button_location)
                    print('Clicking Submit Button')
                    wait(6)
                    
                    # Etapa 6: Locate DDP button
                    ddp_button_location = locate_element('Matching clicker/Img/ddp_button.png')
                    if ddp_button_location:
                        click_at(*ddp_button_location)
                        print('Clicking ddp Button')
                        wait(6)




                    #click_at(1936, 842)
                    else:
                        print("Botão 'ddp' não encontrado.")
                else:
                    print("Botão 'Submit' não encontrado.")
            else:
                print("Opção 'Missing Technical Skills' não encontrada.")
        else:
            print("Botão 'Discard' não encontrado.")
    elif pressed_key == second_key:
        print("Performing alternate action...")
        # Alternate Action 1: Click at empty screen
        click_at(2466, 838)
        # Alternate Action 2: Click at selection box
        click_at(1446, 838)
        # Alternate Action 3: Locate "Request Job Interest" button and click
        request_interest_location = locate_element('Matching clicker/Img/request_interest_button.png')
        if request_interest_location:
            click_at(*request_interest_location)
            print('Clicking Request Job Interest Button')
            wait(4)
        # Alternate Action 4: Locate "Send Correspondence" button and click
        send_correspondence_location = locate_element('Matching clicker/Img/send_correspondence_button.png')
        if send_correspondence_location:
            click_at(*send_correspondence_location)
            print('Clicking Send Correspondence Button')
            wait(4)
            click_at(1936, 842)
    else:
        print("Press the assigned keys to start the script or perform alternate action.")
