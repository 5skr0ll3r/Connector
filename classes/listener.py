import socket,threading


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

	def run(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#self.socket.setblocking(0)
		self.socket.bind((self.interface,self.port))
		self.socket.listen()


	async def accept(self):
		self.connection, self.address = self.socket.accept()

	async def receive(self):
		self.dataReceived = self.connection.recv(3000).decode('utf-8')
		return self.dataReceived

	def respond(self,data):
		self.connection.sendall(data.encode())

	def reconnect(self,_name):
		pass
		#will save the connections info somewhere locally 
		#and if reconnect is triggered we will specify the name given
		#to the saved connection and try to reconnect to the waiting reverse shell
		#this will help if a connection is lost, or incase of a backdoor on the target
		#system, this requires that the reverse shell used will have the wait for reconnection feature
		#so by default  this will be not used
		#ill make some sample reverse shells that will work fine with this functionality

	def close(self):
		self.socket.close()
