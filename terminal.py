from classes.daemon import Daemon
from classes.coloring import Colorer
from classes.parser import Parser
import asyncio,sys,re,os
from time import sleep

class Terminal:

	
	commands = {
	
		'help' : {
			'details' : f'Help is on the way\n\thelp <command>',
			'min_args' : 0,
			'max_args' : 1
		},

		'connect' : {
			'details' : f'Connect to a remote host \n\tconnect <IP> <Server_Port> <Alias>',
			'min_args' : 3,
			'max_args' : 3
		},
		'listen' : {
			'details' : f'Start a listener on specified interface and port and await remote connection \n\tlisten <IP/interface> <Port> <Alias>',
			'min_args' : 3,
			'max_args' : 3
		},	

		'sessions' : {
			'details' : f'Sessions of machines that you have succesfully accessed.',
			'min_args' : 0,
			'max_args' : 0
		},
			
		'shell' : {
			'details' : f'Enable an interactive pseudo-shell for a session. Type back to background the session. \n\tshell <Alias>',
			'min_args' : 1,
			'max_args' : 1
		},						

		'kill' : {
			'details' : f'Terminate a session. \n\tkill <Alias>',
			'min_args' : 1,
			'max_args' : 1
		},		

		'clear' : {
			'details' : f'Clears the screen?.',
			'min_args' : 0,
			'max_args' : 0
		},

		'exit' : {
			'details' : f'Kill all sessions and quit.',
			'min_args' : 0,
			'max_args' : 0
		},
	
	}
	@staticmethod
	def isValid(command, num_of_args):
		
		isValid = True
		
		if command not in Terminal.commands:
			print('Unknown command.')
			isValid = False
			
		elif num_of_args < Terminal.commands[command]['min_args']:
			print('Missing arguments.\nType help <command> to get more information')
			isValid = False
		
		elif num_of_args > Terminal.commands[command]['max_args']:
			print('Too many arguments.')
			isValid = False			
	
		return isValid

	@staticmethod
	def printHelp():
		for i in Terminal.commands:
			print(f"\n{i}")
			for x in Terminal.commands[i]:
				print(f"\t{x}: {Terminal.commands[i][x]}")


	@staticmethod
	def commHelp(command):
		print(f"\n{command}:")
		for i in Terminal.commands[command]:
			print(f"\t{i}: {Terminal.commands[command][i]}")



async def main():

	colorer = Colorer()
	colorer.pokey("Initiating daemon...")
	daemon = Daemon()
	colorer.pokey("daemon initiated")

	while True:
		try:
			colorer.pshell(">")
			sys.stdout.flush()
			userInput = sys.stdin.readline()

			if userInput == "\n":
				continue

			splited = userInput.split(" ")
			for i in range(0,len(splited)):
				if splited[i] == "":
					splited.pop(i)

			if Terminal.isValid(splited[0].strip(),len(splited)-1):

				if "help" in splited[0]:
					if len(splited) > 1:
						Terminal.commHelp(splited[1].strip())
					else:
						Terminal.printHelp()

				if "connect" in splited[0]:
					(ip, port, alias, typ) = (splited[1],splited[2],splited[3],1)
					if Parser.ipCheck(ip) and Parser.portCheck(port):
						await daemon.createNew(alias,typ,ip,port)
						while True:
							command = sys.stdin.readline()
							if "back" in command or "exit" in command:
								daemon.pauseThread()
								break

							daemon.passData(command)
							sleep(.2)
							try:
								data = await daemon.getData()
								sys.stdout.write(data)
							except TypeError:
								break
				if "listen" in splited[0]:
					(ip, port,alias,typ) = (splited[1],splited[2],splited[3],0)
					if Parser.ipCheck(ip) and Parser.portCheck(port):
						await daemon.createNew(alias,typ,ip,port)
						while True:
							command = sys.stdin.readline()
							if "back" in command or "exit" in command:
								daemon.pauseThread()
								break
							daemon.passData(command)
							sleep(.2)
							try:
								data = await daemon.getData()
								sys.stdout.write(data)
							except TypeError:
								break

				if "sessions" in splited[0]:
					daemon.listConnections()

				if "shell" in splited[0]:
					alias = splited[1]
					daemon.changeActive(alias)
					daemon.unpauseThread(alias)
					while True:
						command = sys.stdin.readline()
						if "back" in command:
							daemon.pauseThread()
							break
						if "kill" in command:
							daemon.kill(alias)
							break
						daemon.passData(command)
						sleep(.2)
						try:
							data = await daemon.getData()
							sys.stdout.write(data)
						except TypeError:
							break

				if "kill" in splited[0]:
					daemon.kill(alias)

				if "clear" in splited[0]:
					os.system("clear")

				if "exit" in splited[0]:
					daemon.killAll()
					sys.exit("Exited succesfully")

		except KeyboardInterrupt:
			daemon.killAll()
				


if __name__ == '__main__':
	asyncio.run(main())