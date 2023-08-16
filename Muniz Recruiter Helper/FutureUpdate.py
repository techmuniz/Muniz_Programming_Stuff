import pyautogui
import keyboard
import cv2
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt5.QtGui import QFont

class GUIApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.user_keys = {
            "Salvar Perfil no Projeto": "",
            "Ocultar Perfil do Candidato": "",
            "Candidato Anterior": "",
            "Candidato Seguinte": "",
            "Exibir Mais Experiências": ""
        }

        self.is_automation_running = False

        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Muniz Recruiter Helper")

        layout = QGridLayout()

        self.label = QLabel("Configure as teclas:")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(self.label, 0, 0, 1, 2)

        row = 1
        for action in self.user_keys:
            label = QLabel(f"Tecla para '{action.capitalize()}':")
            label.setFont(QFont("Arial", 12))
            key_input = QLineEdit()
            key_input.setFont(QFont("Arial", 12))
            layout.addWidget(label, row, 0)
            layout.addWidget(key_input, row, 1)
            key_input.textChanged.connect(lambda text, action=action: self.update_key(action, text))
            row += 1

        self.start_button = QPushButton("Iniciar/Pausar Automação")
        self.start_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.start_button.clicked.connect(self.toggle_automation)
        layout.addWidget(self.start_button, row, 0, 1, 2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            background-color: #F0F0F0; /* Background color */
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
        """Update the user-configured keybinding for a specific action."""
        if self.validate_key(key):
            self.user_keys[action] = key
        else:
            self.show_key_warning()

    def validate_key(self, key):
        """Validate that a keybinding consists of a single letter or number."""
        return len(key) == 1 and (key.isalpha() or key.isnumeric())

    def show_key_warning(self):
        """Show a warning message when an invalid keybinding is entered."""
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setWindowTitle("Aviso")
        warning_box.setText("A tecla inserida é inválida. Insira uma única letra ou número.")
        warning_box.exec_()

    def toggle_automation(self):
        """Toggle the automation process."""
        if not self.is_automation_running:
            self.is_automation_running = True
            self.start_button.setText("Pausar Automação")
            self.automation_thread = threading.Thread(target=self.start_automation_thread)
            self.automation_thread.start()
            self.show_user_feedback("Automação iniciada.")
        else:
            self.is_automation_running = False
            self.start_button.setText("Iniciar/Pausar Automação")
            self.show_user_feedback("Automação pausada.")

    def start_automation_thread(self):
        """Start the thread for automation."""
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
            self.start_button.setText("Iniciar/Pausar Automação")
            self.show_user_feedback(f"Erro na automação: {str(e)}")

    def perform_action(self, action):
        """Perform a specific action based on the user's keybinding."""
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
            self.process_image("Muniz Recruiter Helper/Images/Exibir Mais Experiencias2.png")
            self.process_image("Muniz Recruiter Helper/Images/Exibir Mais Experiencias3.png")
            print("Exibir Mais Experiências")

    def scroll_and_process(self, action_name):
        """Scroll and process based on the action."""
        pyautogui.scroll(4000)
        time.sleep(0.5)
        pyautogui.scroll(4000)
        time.sleep(0.5)
        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}.png")
        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}2.png")
        self.process_image("Muniz Recruiter Helper/Images/Candidato Seguinte.png")
        print(f"{action_name} Perfil")

    def process_image(self, image_path):
        """Process an image and perform a click action if found on screen."""
        image = cv2.imread(image_path)
        coordinates = pyautogui.locateOnScreen(image, confidence=0.8)
        if coordinates:
            pyautogui.click(coordinates)

    def edit_keys(self):
        """Edit user-configured keybindings."""
        print("\nEditando teclas:")
        for action in self.user_keys:
            key_input = QLineEdit()
            new_key = key_input.text()
            if new_key:
                self.user_keys[action] = new_key

    def show_user_feedback(self, message):
        """Show user feedback using a message box."""
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
