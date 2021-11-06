from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_PyMessanger import Ui_MainWindow
import sys

class server(QMainWindow):
    def __init__(self):
        self.text = ""
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.send_button.clicked.connect(self.send)
        self.show()
    def send(self):
        self.text += self.ui.entry.toPlainText()
        self.ui.textEdit.setText(self.text)
        self.ui.entry.setText("")
        self.text += "\n"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = server()
    sys.exit(app.exec_())
