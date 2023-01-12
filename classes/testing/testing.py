from time import sleep
import threading 

class Test:
	def __init__(self,daemon,_name):
		self.name = _name
		self.tes = "It Works"
		self.set = "not set"
		self.daemon = daemon

	def chSet(self):
		self.daemon.store(self)
		self.test()

	def test(self):
		while True:
			print(self.set)
			sleep(2)


	


class Daemon:
	def __init__(self):
		self.data = "datara"
		self.threadList = []

	def store(self,threadself):
		self.threadList.append(threadself)
		self.threadList[0].set = "is set"
		print(self.threadList[0].set)

	def getIndex(self,_name):
		for i in self.threadList:
			if i.name == _name:
				return i

	def chSet(self,_lis):
		for i in _lis:
			sleep(4)
			self.threadList[0].set = f"{i}"
		return


def main():
	lis = ["is set", "is d","fds","fdasassa","aaa"]
	daemon = Daemon()
	test = Test(daemon,"skata")
	test2 = Test(daemon,"skatenia")
	t1 = threading.Thread(target=test.chSet)
	t2 = threading.Thread(target=daemon.chSet, args=[lis])
	t1.start()
	t2.start()

	for i in range(30):
		print(i)
		sleep(2)

if __name__ == '__main__':
	main()