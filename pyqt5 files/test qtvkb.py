import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class VirtualKeyboardExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create QLineEdit for text input
        self.text_entry = QLineEdit()
        self.text_entry.setAlignment(Qt.AlignCenter)

        # Create a QQuickView for the virtual keyboard
        qml_view = QQuickView()
        qml_engine = qml_view.engine()
        qml_component = qml_engine.createComponent(QUrl.fromLocalFile(':/QtQuick/VirtualKeyboard.qml'))

        # Check if the QML component was successfully created
        if qml_component.isError():
            print("Error loading Virtual Keyboard QML component:", qml_component.errors())
            sys.exit(-1)

        # Create QWebEngineView and set the QML component as its content
        web_view = QWebEngineView()
        web_view.setResizeMode(QWebEngineView.SizeRootObjectToView)
        web_view.page().setWebChannel(qml_view.rootContext().channel())
        web_view.setSource(QUrl.fromLocalFile(':/QtQuick/VirtualKeyboard.qml'))

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_entry)
        layout.addWidget(web_view)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the text_entry editingFinished signal to a function
        self.text_entry.editingFinished.connect(self.on_text_entry_finished)

        # Set window properties
        self.setWindowTitle('Qt Virtual Keyboard Example')
        self.setGeometry(100, 100, 400, 200)

    def on_text_entry_finished(self):
        entered_text = self.text_entry.text()
        print('Text entry finished. Entered text:', entered_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VirtualKeyboardExample()
    window.show()
    sys.exit(app.exec_())
