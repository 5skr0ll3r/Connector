from classes.daemon import Daemon
import asyncio


async def main():
	print("Initiating daemon...\n")
	daemon = Daemon()
	print("daemon initiated\n")

	while True:
		print("Choose action:\n0: Create listener/client\n1: List active connections\n2: Manage running\n3: Leave")
		choice = int(input("> "))

		if choice == 0:
			ip = input("IP: ")
			port = input("Port: ")
			name = input("Name: ")
			typ = input("Type of connection (0/1): ")
			await daemon.createNew(name,typ,ip,port)
			while True:
				command = input(f"{name}> ")
				if command == "back":
					daemon.pauseThread(name)
					break
				if command == "kill":
					daemon.kill()
					break
				daemon.passData(command)
				data = await daemon.getData()
				print(data)

		if choice == 1:
			daemon.listConnections()

		if choice == 2:
			name = input("Name: ")
			daemon.changeActive(name)
			daemon.unpauseThread(name)
			while True:
				command = input(f"{name}> ")
				if command == "back":
					daemon.pauseThread(name)
					break
				if command == "kill":
					daemon.kill()
					break
				daemon.passData(command)
				data = await daemon.getData()
				print(data)

		if choice == 3:
			daemon.killAll()
				


if __name__ == '__main__':
	asyncio.run(main())