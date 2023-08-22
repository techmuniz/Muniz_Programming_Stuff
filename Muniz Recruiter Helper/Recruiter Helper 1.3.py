import pyautogui
import keyboard
import cv2
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QColor

class GUIApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.user_keys = {
            "Save in Project": "",
            "Hide Candidate Profile": "",
            "Previous Candidate": "",
            "Next Candidate": "",
            #"Show More Experience": ""
        }

        self.is_automation_running = False

        self.color_not_started = QColor(255, 255, 204)  # Light cream
        self.color_started = QColor(144, 238, 144)   # Light Green

        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
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
        warning_box.setText("Insert just one Key. It can be ALphanumeric or Numeric. If you insert more than one, it will not function correctly.")
        warning_box.exec_()

    def toggle_automation(self):
        """Toggle the automation process."""
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
            self.start_button.setText("Iniciate/Pause Automation")
            self.show_user_feedback(f"Automation Error: {str(e)}")

    def perform_action(self, action):
        """Perform a specific action based on the user's keybinding."""
        if action == "Hide Candidate Profile":
            self.scroll_and_process("Hide Candidate Profile")

        elif action == "Save in Project":
            self.scroll_and_process("Save in Project")

        elif action == "Previous Candidate":
            #self.process_image("Muniz Recruiter Helper/Images/Candidato Anterior.png") -- Old Way
            self.scroll_and_process_Next_Previous("Previous Candidate")
            #print("Candidato Anterior")

        elif action == "Next Candidate":
            #self.process_image("Muniz Recruiter Helper/Images/Candidato Seguinte.png") -- Old Way
            self.scroll_and_process_Next_Previous("Next Candidate")
            #print("Candidato Seguinte")

        '''elif action == "Show More Experience":
            self.process_image("Muniz Recruiter Helper/Images/Show More80.png")
            self.process_image("Muniz Recruiter Helper/Images/Show More90.png")
            self.process_image("Muniz Recruiter Helper/Images/Show More100.png")
            self.process_image("Muniz Recruiter Helper/Images/Show More110.png")
            print("Show More Experience")'''

    def scroll_and_process(self, action_name):
        """Scroll and process based on the action."""
        pyautogui.scroll(4000)
        time.sleep(0.5)
        pyautogui.scroll(4000)
        time.sleep(0.5)

        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}80.png")
        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}90.png")
        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}100.png")
        self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}110.png")
        self.process_image("Muniz Recruiter Helper/Images/NextCandidadeSingle.png")
        print(f"{action_name}")

    def scroll_and_process_Next_Previous(self, action_name):
        """Scroll and process based on the action."""
        pyautogui.scroll(4000)
        time.sleep(0.5)
        pyautogui.scroll(4000)
        time.sleep(0.5)

        previous_processed = True  # Flag to track if the previous image was processed successfully
        
        if not self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}80.png"):
            previous_processed = False
            
        if previous_processed and not self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}90.png"):
            previous_processed = False
            
        if previous_processed and not self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}100.png"):
            previous_processed = False
            
        if previous_processed and not self.process_image(f"Muniz Recruiter Helper/Images/{action_name.lower()}110.png"):
            previous_processed = False

        if previous_processed:
            print(f"{action_name} Profile")

        # Different from the previous function scroll_and_process, here we have to process the time just one time,
        # otherwise we would be processing the same image more than one time, and this would make us skip some profiles.

    def process_image(self, image_path):
        """Process an image and perform a click action if found on screen."""
        image = cv2.imread(image_path)
        coordinates = pyautogui.locateOnScreen(image, confidence=0.65)
        if coordinates:
            x, y, width, height = coordinates
            
            # Calculating the new X coordinate closer to the center (20% towards the center)
            x_center = x + int(width * 0.2)
            y_center = y + (height // 2)  # Keeping the same Y coordinate for vertical center
            
            # Performing the click at the new coordinate
            pyautogui.click(x_center, y_center)
        else:
            print(f"Image not found: {image_path}")
            # Print the coordinates for debugging
            print("Coordinates:", coordinates)
                  
            # It was necessary to make this adjustment (not click in the center of the image) because if the click was performed in 
            # the center, when we wanted to save the profile in the project, the click was performed in the "Show more options" button, 
            # but the profile was not saved.

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
