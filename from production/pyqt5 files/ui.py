import os
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit

class SimpleUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        label = QLabel('Enter text:')
        self.text_entry = QLineEdit()
        button = QPushButton('Click me!')

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.text_entry)
        layout.addWidget(button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect button click event to a function
        button.clicked.connect(self.on_button_click)

        # Set window properties
        self.setWindowTitle('Simple PyQt5 UI')
        self.setGeometry(100, 100, 300, 200)

    def on_button_click(self):
        # Get the text from the entry and print it
        entered_text = self.text_entry.text()
        print('Button clicked! Entered text:', entered_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec_())
