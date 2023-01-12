import socket


class Client:
	def __init__(self, _target,_port):

		if(_target == None):
			self.target = "127.0.0.1"
		else: 
			self.target = _target

		if(_port == None):
			self.port = 8080
		else:
			self.port = int(_port)
		
		self.dataReceived = None
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	def connect(self):
		self.socket.connect((self.target,self.port))

	async def receive(self):
		self.dataReceived =  self.socket.recv(4096).decode('utf-8')
		return self.dataReceived

	def respond(self,data):
		self.socket.sendall((data).encode())

	def close(self):
		self.socket.close()
