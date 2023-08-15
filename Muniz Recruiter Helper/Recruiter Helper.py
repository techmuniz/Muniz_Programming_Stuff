import pyautogui
import keyboard
import cv2
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class GUIApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.user_keys = {
            "Ocultar Perfil do Candidato": "",
            "Salvar Perfil no Projeto": "",
            "Candidato Anterior": "",
            "Candidato Seguinte": "",
            "Exibir Mais Experiências": ""
        }

        self.is_automation_running = False

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Muniz Recruiter Helper")

        layout = QVBoxLayout()

        self.label = QLabel("Configure as teclas:")
        layout.addWidget(self.label)

        for action in self.user_keys:
            key_input = QLineEdit()
            layout.addWidget(QLabel(f"Tecla para '{action.capitalize()}':"))
            layout.addWidget(key_input)
            key_input.textChanged.connect(lambda text, action=action: self.update_key(action, text))

        self.reset_button = QPushButton("Resetar Teclas")
        self.reset_button.clicked.connect(self.reset_keys)
        layout.addWidget(self.reset_button)

        self.start_button = QPushButton("Iniciar Automação")
        self.start_button.clicked.connect(self.toggle_automation)
        layout.addWidget(self.start_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_key(self, action, key):
        self.user_keys[action] = key

    def reset_keys(self):
        for action in self.user_keys:
            self.user_keys[action] = ""

    def toggle_automation(self):
        if not self.is_automation_running:
            self.is_automation_running = True
            self.automation_thread = threading.Thread(target=self.start_automation_thread)
            self.automation_thread.start()
        else:
            self.is_automation_running = False

    def start_automation_thread(self):
        while self.is_automation_running:
            for action, key in self.user_keys.items():
                if key and keyboard.is_pressed(key):
                    self.perform_action(action)
                    time.sleep(0.5)

            if keyboard.is_pressed("0"):
                self.edit_keys()

    def perform_action(self, action):
        if action == "Ocultar Perfil do Candidato":
            self.scroll_and_process("Ocultar Perfil do Candidato")
        elif action == "Salvar Perfil no Projeto":
            self.scroll_and_process("Salvar Perfil no Projeto")
        elif action == "Candidato Anterior":
            self.process_image("Muniz Recruiter Helper/Images/Candidato Anterior.png")
            print("Candidato Anterior")
        elif action == "Candidato Seguinte":
            self.process_image("Muniz Recruiter Helper/Images/Candidato Seguinte.png")
            print("Candidato Seguinte")
        elif action == "Exibir Mais Experiências":
            self.process_image("Muniz Recruiter Helper/Images/Exibir Mais Experiencias.png")
            print("Exibir Mais Experiências")

    def scroll_and_process(self, action_name):
        pyautogui.scroll(4000)
        time.sleep(0.5)
        pyautogui.scroll(4000)
        time.sleep(0.5)
        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}.png")
        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}2.png")
        self.process_image("Muniz Recruiter Helper/Images/Candidato Seguinte.png")
        print(f"{action_name} Perfil")

    def process_image(self, image_path):
        image = cv2.imread(image_path)
        coordinates = pyautogui.locateOnScreen(image, confidence=0.8)
        if coordinates:
            pyautogui.click(coordinates)

    def edit_keys(self):
        print("\nEditando teclas:")
        for action in self.user_keys:
            key_input = QLineEdit()
            new_key = key_input.text()
            if new_key:
                self.user_keys[action] = new_key

if __name__ == "__main__":
    app = QApplication([])
    window = GUIApp()
    window.show()
    app.exec_()
