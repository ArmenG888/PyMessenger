import socket,threading,time,random
class server:
	def __init__(self):
		self.name = "Armen"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(("127.0.0.1",52000))
		s.listen(5)
		self.conn, addr = s.accept()
		recieve = threading.Thread(target=self.recieve)
		recieve.start()
		while True:
			x = input(self.name+":")
			self.conn.send(self.name.encode() +":".encode()+x.encode())
	def recieve(self):
		while True:
			data = self.conn.recv(1024).decode()
			print("\n"+data)
app = server()
