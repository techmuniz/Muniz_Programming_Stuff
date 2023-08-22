import pyautogui
import keyboard
import cv2
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QColor
import os
import sys

class GUIApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.user_keys = {
            "Save in Project": "",
            "Hide Candidate Profile": "",
            "Previous Candidate": "",
            "Next Candidate": "",
            "Show More Experience": ""
        }

        self.is_automation_running = False

        self.color_not_started = QColor(255, 255, 204)  # Light cream
        self.color_started = QColor(144, 238, 144)   # Light Green

        # Obtendo o diretório do script em execução
        self.script_directory = os.path.dirname(os.path.abspath(__file__))
        # Construindo o caminho completo para a pasta "Images"
        self.images_directory = os.path.join(self.script_directory, "Images")  # Corrigido aqui

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Muniz Recruiter Helper")

        layout = QGridLayout()

        self.label = QLabel("Set the Keys:")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(self.label, 0, 0, 1, 2)

        row = 1
        for action in self.user_keys:
            label = QLabel(f"Key to '{action.capitalize()}':")
            label.setFont(QFont("Arial", 12))
            key_input = QLineEdit()
            key_input.setFont(QFont("Arial", 12))
            layout.addWidget(label, row, 0)
            layout.addWidget(key_input, row, 1)
            key_input.textChanged.connect(lambda text, action=action: self.update_key(action, text))
            row += 1

        self.start_button = QPushButton("Iniciate Automation")
        self.start_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.start_button.clicked.connect(self.toggle_automation)
        layout.addWidget(self.start_button, row, 0, 1, 2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            background-color: #F0F0F0;
            QLabel { color: #333333; font-size: 14px; }
            QLineEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; padding: 8px; font-size: 12px; }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #2980b9; }
            QMessageBox { background-color: #FFFFFF; color: #333333; }
        """)

    def update_key(self, action, key):
        if self.validate_key(key):
            self.user_keys[action] = key
        else:
            self.show_key_warning()

    def validate_key(self, key):
        return len(key) == 1 and (key.isalpha() or key.isnumeric())

    def show_key_warning(self):
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setWindowTitle("Aviso")
        warning_box.setText("Insert just one Key. It can be ALphanumeric or Numeric. If you insert more than one, it will not function correctly.")
        warning_box.exec_()

    def toggle_automation(self):
        if not self.is_automation_running:
            self.is_automation_running = True
            self.start_button.setText("Pause Automation")
            self.start_button.setStyleSheet(f"background-color: {self.color_started.name()}; color: black;")
            self.automation_thread = threading.Thread(target=self.start_automation_thread)
            self.automation_thread.start()
            print("Automation Started.")
        else:
            self.is_automation_running = False
            self.start_button.setText("Iniciate Automation")
            self.start_button.setStyleSheet(f"background-color: {self.color_not_started.name()}; color: black;")
            print("Automation Paused.")

    def start_automation_thread(self):
        try:
            while self.is_automation_running:
                for action, key in self.user_keys.items():
                    if key and keyboard.is_pressed(key):
                        self.perform_action(action)
                        time.sleep(0.5)

                if keyboard.is_pressed("0"):
                    self.edit_keys()
        except Exception as e:
            self.is_automation_running = False
            self.start_button.setText("Iniciate/Pause Automation")
            self.show_user_feedback(f"Automation Error: {str(e)}")

    def perform_action(self, action):
        if action == "Hide Candidate Profile":
            self.scroll_and_process("Hide Candidate Profile")

        elif action == "Save in Project":
            self.scroll_and_process("Save in Project")

        elif action == "Previous Candidate":
            self.scroll_and_process_Next_Previous("Previous Candidate")

        elif action == "Next Candidate":
            self.scroll_and_process_Next_Previous("Next Candidate")

        elif action == "Show More Experience":
            self.process_image("Show More80.png")
            self.process_image("Show More90.png")
            self.process_image("Show More100.png")
            self.process_image("Show More110.png")
            print("Show More Experience")

    def scroll_and_process(self, action_name):
        pyautogui.scroll(4000)
        time.sleep(0.5)
        pyautogui.scroll(4000)
        time.sleep(0.5)

        self.process_image(f"{action_name.lower()}80.png")
        self.process_image(f"{action_name.lower()}90.png")
        self.process_image(f"{action_name.lower()}100.png")
        self.process_image(f"{action_name.lower()}110.png")
        self.process_image("NextCandidadeSingle.png")
        print(f"{action_name}")

    def scroll_and_process_Next_Previous(self, action_name):
        pyautogui.scroll(4000)
        time.sleep(0.5)
        pyautogui.scroll(4000)
        time.sleep(0.5)

        previous_processed = True
        
        if not self.process_image(f"{action_name.lower()}80.png"):
            previous_processed = False
            
        if previous_processed and not self.process_image(f"{action_name.lower()}90.png"):
            previous_processed = False
            
        if previous_processed and not self.process_image(f"{action_name.lower()}100.png"):
            previous_processed = False
            
        if previous_processed and not self.process_image(f"{action_name.lower()}110.png"):
            previous_processed = False

        if previous_processed:
            print(f"{action_name} Profile")

    def process_image(self, image_filename):

        # Usando o caminho completo para a imagem
        full_image_path = os.path.join(self.images_directory, image_filename)
        image = cv2.imread(full_image_path)
        if image is not None:
            coordinates = pyautogui.locateOnScreen(image, confidence=0.8)
            if coordinates:
                x, y, width, height = coordinates
                x_center = x + int(width * 0.2)
                y_center = y + (height // 2)
                pyautogui.click(x_center, y_center)
            else:
                print(f"Image not found: {image_filename}")
                print("Coordinates:", coordinates)
        else:
            print(f"Error loading image: {image_filename}")

    def edit_keys(self):
        print("\nEditando teclas:")
        for action in self.user_keys:
            key_input = QLineEdit()
            new_key = key_input.text()
            if new_key:
                self.user_keys[action] = new_key

    def show_user_feedback(self, message):
        feedback_box = QMessageBox()
        feedback_box.setIcon(QMessageBox.Information)
        feedback_box.setWindowTitle("Feedback")
        feedback_box.setText(message)
        feedback_box.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = GUIApp()
    window.show()
    app.exec_()
