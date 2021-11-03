import socket
import keyboard
import time
import threading
import random
class client:
	def __init__(self):
		self.name = "test"
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect(("127.0.0.1",52000))
		recieve = threading.Thread(target=self.recieve)
		recieve.start()
		while True:
			x = input(self.name+":")
			self.s.send(self.name.encode() +":".encode()+x.encode())
	def recieve(self):
		while True:
			data = self.s.recv(1024).decode()
			print("\n"+data)
app = client()
