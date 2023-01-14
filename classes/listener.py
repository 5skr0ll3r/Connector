import socket,sys

class Listener:
	def __init__(self, _interface,_port):

		if(_interface == None):
			self.interface = socket.gethostbyname(socket.gethostname())
		else: 
			self.interface = _interface

		if(_port == None):
			self.port = 8080
		else:
			self.port = int(_port)
		
		self.connection = None
		self.address = None
		self.dataReceived = None
		self.socket = None
		self.fail = False

	def run(self):
		try:
			self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.socket.bind((self.interface,self.port))
			self.socket.listen()
		except OSError:
			sys.stdout.write("Something went wrong on listeners creation\nPlease make sure the interface you specified exists\n")
			sys.stdout.flush()
			self.close()
			self.fail = True


	async def accept(self):
		if not self.fail:
			self.connection, self.address = self.socket.accept()
		else:
			self.close()

	async def receive(self):
		if not self.fail:
			self.dataReceived = self.connection.recv(8000).decode('utf-8')#4096
			return self.dataReceived
		else:
			self.close()

	def respond(self,data):
		if not self.fail:
			self.connection.sendall(data.encode())
		else:
			self.close()

	def close(self):
		self.socket.close()
