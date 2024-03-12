import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

class VirtualKeyboardExample(QQuickView):
    def __init__(self):
        super().__init__()

        view = QQuickView()
        view.setSource(QUrl.fromLocalFile('.\pyqt5 files\VB.qml'))


    def init_ui(self):
        # Create a QWebEngineView for the virtual keyboard
        web_view = QWebEngineView()
        web_view.setUrl(QUrl.fromLocalFile('./VB.qml'))

        # # Create layout
        # layout = QVBoxLayout()
        # layout.addWidget(web_view)

        # # Set the layout for the main window
        # self.setLayout(layout)

        # Set window properties
        # self.setWindowTitle('Qt Virtual Keyboard Example')
        # self.setGeometry(1000, 1000, 50, 50)

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    app = QGuiApplication(sys.argv)
    window = VirtualKeyboardExample()
    window.show()
    sys.exit(app.exec_())
