import sys
class Colorer:
	def __init__(self):
		self.Pref = "\033["
		self.NC = "\033[0m"
		self.red = "0;31m"
		self.green = "0;32m"
		self.blue = "0;34m"
		self.liBlue = "1;34m"
		
	def pmenu(self,data):
		sys.stdout.write(self.Pref+self.blue+data+self.NC+'\n')
		sys.stdout.flush()
	def pshell(self,data):
		sys.stdout.write(self.Pref+self.liBlue+data+self.NC+" ")
		sys.stdout.flush()
	def pokey(self,data):
		sys.stdout.write(self.Pref+self.green+data+self.NC+'\n')
		sys.stdout.flush()
	def perror(self,data):
		sys.stdout.write(self.Pref+self.red+data+self.NC+'\n')
		sys.stdout.flush()

	@staticmethod
	def logo():
		sys.stdout.write("""Conector""")




logo = """
---------------------------------------------------------------------
--------/-/----------------------------------------------------------
-------/-/-----------------------------------------------------------
------|-|------------------------------------------------------------
------\\-\\-----------------------------------------------------------
-------\\-\\----------------------------------------------------------
--------\\-\\---------------------------------------------------------
---------------------------------------------------------------------
"""