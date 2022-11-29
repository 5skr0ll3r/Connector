from classes.client import Client
from classes.listener import Listener
import threading, asyncio

class Thread(threading.Thread):
	def __init__(self,daemon,_name,_type=0,_address=None,_port=None):
		threading.Thread.__init__(self)
		self.name = _name
		self.type = int(_type) # 0 or 1 (listener or client)
		self.paused = False
		self.killed = False
		self.connection = None
		self.address = _address
		self.port = _port
		self.daemon = daemon
		self.start()


	def connect(self):
		self.daemon.store(self)

	async def create(self):
		if self.type == 0:
			self.connection = Listener(self.address,self.port)
			self.connection.run()
			await self.connection.accept()

		elif self.type == 1:
			self.connection = Client(self.address,self.port)
			self.connection.connect()
		else:
			print("Wrong Socket Type either 0 or 1")
			pass

	def send(self,_data):
		if not self.paused:
			self.connection.respond(_data)
		else:
			pass

	async def receive(self):
		if not self.paused:
			return await self.connection.receive()
		else:
			pass


	def pause(self):
		self.paused = True
	def unpause(self):
		self.paused = False


	def kill(self):
		self.connection.close()
		return

	async def start(self):
		self.connect()
		await self.create()