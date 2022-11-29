from classes.thread import Thread
import asyncio,sys

class Daemon:
	def __init__(self):
		self.threadList = []
		self.activeIndex = 0

	def store(self,threadself):
		self.threadList.append(threadself)

	async def createNew(self,_name,_type,_address,_port):
		await Thread(self,_name,_type,_address,_port).start()
		self.changeActive(_name)

	def getIndex(self,_name):
		for i in range(0,len(self.threadList)):
			if self.threadList[i].name == _name:
				return i

	def listConnections(self):
		for i in self.threadList:
			print(f"Name: {i.name} Type: {i.type} Address: {i.address} Port {i.port}\n")

	def changeActive(self,_name):
		self.activeIndex = self.getIndex(_name)

	def printThreadList(self):
		for i in self.threadList:
			print(i)

	def passData(self,_data):
		self.threadList[self.activeIndex].send(_data)

	async def getData(self):
		return await self.threadList[self.activeIndex].receive()

	def pauseThread(self,_name):
		self.threadList[self.activeIndex].pause()

	def unpauseThread(self,_name):
		self.threadList[self.activeIndex].unpause()

	def kill(self):
		self.threadList[self.activeIndex].kill()
		self.threadList.pop(self.activeIndex)
		return

	def killAll(self):
		if len(self.threadList) > 0:
			for i in self.threadList:
				i.kill()
		return sys.exit("Exited succesfully")