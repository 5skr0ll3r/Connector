import sys

class Parser:

	@staticmethod
	def ipCheck(ip):
		nums = ip.replace(".","")
		if nums.isnumeric():
			splited = ip.split(".")
			if len(splited) == 4 and int(splited[0]) >= 0 and int(splited[0]) <= 254 and int(splited[1]) >= 0 and int(splited[1]) <= 254 and int(splited[2]) >= 0 and int(splited[2]) <= 254 and int(splited[3]) >= 0 and int(splited[3]) <= 254:
				return True
			else:
				sys.stdout.write("Ip out of range\n")
				sys.stdout.flush()
				return False
		else:
			sys.stdout.write("Illegal character/s in ip\n")
			sys.stdout.flush()
			return False

	@staticmethod
	def portCheck(port):
		if port.isnumeric():
			return True
		else:
			sys.stdout.write("Illegal character/s in port\n")
			sys.stdout.fluash()
			return False
