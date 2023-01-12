from classes.thread import Thread
import sys

class Daemon:
	def __init__(self):
		self.threadList = []
		self.activeIndex = 0

	def store(self,threadself):
		self.threadList.append(threadself)

	def exists(self,_alias):
		if len(self.threadList) > 0:
			for i in self.threadList:
				if i.alias == _alias:
					return True
			return False
		else: return False

	async def createNew(self,_alias,_type,_address,_port):
		if not self.exists(_alias):
			await Thread(self,_alias,_type,_address,_port).start()
			self.changeActive(_alias)
			if self.threadList[self.activeIndex].failed:
				self.kill(_alias)
		else:
			sys.stdout.write(f"Alias: {_alias} already in use\ndo sessions to see the names you are using")
			sys.stdout.flush()

	def getIndex(self,_alias):
		if self.exists(_alias):
			for i in range(0,len(self.threadList)):
				if self.threadList[i].alias == _alias:
					return i

	def listConnections(self):
		if len(self.threadList) > 0:
			for i in self.threadList:
				print(f"Alias: {i.alias} Type: {i.type} Address: {i.address} Port {i.port}\n")
		else:
			sys.stdout.write("List is Empty\n")
			sys.stdout.flush()

	def changeActive(self,_alias):
		if self.exists(_alias):
			self.activeIndex = self.getIndex(_alias)
		else:
			sys.stdout.write("Does not exist\n")
			sys.stdout.flush()
			return

	def printThreadList(self): #For Debugging
		for i in self.threadList:
			print(i)

	def passData(self,_data):
		if self.activeIndex < len(self.threadList):
			self.threadList[self.activeIndex].send(_data)
		else: return

	async def getData(self):
		if self.activeIndex < len(self.threadList):
			return await self.threadList[self.activeIndex].receive()
		else: return

	def pauseThread(self):
		self.threadList[self.activeIndex].pause()

	def unpauseThread(self,_alias):
		if self.exists(_alias):
			self.threadList[self.activeIndex].unpause()

	def kill(self,_alias):
		self.threadList[self.getIndex(_alias)].kill()
		self.threadList.pop(self.activeIndex)
		return

	def killAll(self):
		if len(self.threadList) > 0:
			for i in self.threadList:
				i.kill()
		return sys.exit("Exited succesfully")

# 11555