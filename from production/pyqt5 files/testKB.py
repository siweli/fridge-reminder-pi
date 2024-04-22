import os
os.environ["QT_DIR"] = "/opt/Qt5.8.0/5.8/gcc_64"
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/opt/Qt5.8.0/5.8/gcc_64/plugins/platforms"
os.environ["QT_PLUGIN_PATH"] = "/opt/Qt5.8.0/5.8/gcc_64/plugins"
os.environ["QML_IMPORT_PATH"] = "/opt/Qt5.8.0/5.8/gcc_64/qml"
os.environ["QML2_IMPORT_PATH"] = "/opt/Qt5.8.0/5.8/gcc_64/qml"
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

class VirtualKeyboardExample(QQuickView):
    def __init__(self):
        super().__init__()

        view = QQuickView()
        view.setObjectName("View")
        # view.setSource(QUrl.fromLocalFile('.\pyqt5 files\VB.qml'))
        view.setSource(QUrl('.\pyqt5 files\VB.qml'))

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    window = VirtualKeyboardExample()
    window.show()
    sys.exit(app.exec_())