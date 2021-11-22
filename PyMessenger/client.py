import socket,time,threading,random,sys
from win10toast import ToastNotifier
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_PyMessanger import Ui_MainWindow
from ui_join_page import Ui_MainWindow as join_page
class client(QMainWindow):
	def __init__(self):
		with open("INFO","r") as r:
			r = r.read()
			r = r.split(",")
		QMainWindow.__init__(self)
		self.ui = join_page()
		self.ui.setupUi(self)
		self.ui.join_button.clicked.connect(self.join)
		if len(r) == 3:
			self.ui.username_entry.setText(r[0])
			self.ui.ip_entry.setText(r[1])
			self.ui.port_entry.setText(r[2])
		self.show()
	def join(self):
		with open("INFO","w+") as r:
			r.write(self.ui.username_entry.text()+","+ self.ui.ip_entry.text() +","+self.ui.port_entry.text())
		self.name = self.ui.username_entry.text()
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.ui.ip_entry.text(),int(self.ui.port_entry.text())))
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
			self.ui.listWidget.addItem(self.username +":"+ data + "\n")
			toaster = ToastNotifier()
			toaster.show_toast("New Message",self.username +":"+ data + "\n")
	def send(self):
		self.ui.listWidget.addItem(self.name +":" + self.ui.entry.toPlainText() + "\n")
		self.s.send(self.ui.entry.toPlainText().encode())
		self.ui.entry.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = client()
    sys.exit(app.exec_())
