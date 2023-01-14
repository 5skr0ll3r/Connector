from classes.daemon import Daemon
from classes.coloring import Colorer
from classes.parser import Parser
from classes.terminal import Terminal
import asyncio,sys,re,os
from time import sleep

async def main():

	colorer = Colorer()
	colorer.pokey("Initiating daemon...")
	daemon = Daemon()
	colorer.pokey("daemon initiated")
	history = []
	while True:
		try:
			colorer.pshell(">")
			sys.stdout.flush()
			userInput = sys.stdin.readline()
			if len(history) >= 15:
				history.pop(15)
			history.append(userInput)

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