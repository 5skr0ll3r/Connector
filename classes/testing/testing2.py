import socket, sys, asyncio,time



async def receive(connection):
	return connection.recv(4096).decode('utf-8')


async def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(("127.0.0.1", 4444))
	s.listen()
	connection, address = s.accept()
	while True:
		data = await receive(connection)
		sys.stdout.write(data)
		#msg = sys.stdin.readline()
		#connection.sendall(msg.encode())		
		connection.sendall(sys.stdin.readline().encode())
		time.sleep(.2)

if __name__ == '__main__':
	asyncio.run(main())