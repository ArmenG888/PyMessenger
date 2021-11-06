import socket,time,threading,random,sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_PyMessanger import Ui_MainWindow

class client(QMainWindow):
	def __init__(self):
		self.text = ""
		self.name = "testuser1"
		QMainWindow.__init__(self)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect(("127.0.0.1",52001))
		self.s.send(self.name.encode())
		self.username = self.s.recv(1024).decode()
		recieve = threading.Thread(target=self.recieve)
		recieve.start()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.send_button.clicked.connect(self.send)
		self.show()
	def recieve(self):
		while True:
			data = self.s.recv(1024).decode()
			self.text += self.username +":"+ data + "\n"
			self.ui.textEdit.setText(self.text)
	def send(self):
		self.text += self.name +":" + self.ui.entry.toPlainText() + "\n"
		self.ui.textEdit.setText(self.text)
		self.s.send(self.ui.entry.toPlainText().encode())
		self.ui.entry.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = client()
    sys.exit(app.exec_())
