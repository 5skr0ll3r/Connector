from classes.daemon import Daemon
from classes.coloring import Colorer
import asyncio,sys
from time import sleep

async def main():
	colorer = Colorer()
	colorer.pokey("Initiating daemon...")
	daemon = Daemon()
	colorer.pokey("daemon initiated")

	while True:
		colorer.pmenu("Choose action:\n0: Create listener/client\n1: List active connections\n2: Manage running\n3: Leave")
		colorer.pshell(">")
		sys.stdout.flush()
		choice = int(sys.stdin.readline())
		match choice:
			case 0:
				ip = input("IP: ")
				port = input("Port: ")
				name = input("Name: ")
				typ = input("Type of connection (0/1): ")
				await daemon.createNew(name,typ,ip,port)
				while True:
					command = sys.stdin.readline()
					if "back" in command :
						daemon.pauseThread(name)
						break
					if "kill"in command:
						daemon.kill()
						break
					daemon.passData(command)
					sleep(.2)
					data = await daemon.getData()
					sys.stdout.write(data)

			case 1:
				daemon.listConnections()

			case 2:
				name = input("Name: ")
				daemon.changeActive(name)
				daemon.unpauseThread(name)
				while True:
					command = sys.stdin.readline()
					if "back" in command:
						daemon.pauseThread(name)
						break
					if "kill" in command:
						daemon.kill()
						break
					daemon.passData(command)
					sleep(.2)
					data = await daemon.getData()
					sys.stdout.write(data)

			case 3:
				daemon.killAll()
			case _:
				sys.stdout.write("Wrong input format")
				sys.stdout.flush()
				continue	


if __name__ == '__main__':
	asyncio.run(main())