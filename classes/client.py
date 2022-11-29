import socket, asyncio, threading


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
		self.dataReceived =  self.socket.recv(3000).decode('utf-8')
		return self.dataReceived

	def respond(self,data):
		self.socket.sendall((data).encode())

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
