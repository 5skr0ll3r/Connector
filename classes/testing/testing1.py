import socket, os, sys

def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(("127.0.0.1", 4444))
	s.listen()
	connection, address = s.accept()
	sock_list = [sys.stdin,connection]
	while True:
		for i in sock_list:
			if i == connection:
				data = connection.recv(3000).decode('utf-8')
				if (not data):
					continue
				else:
					sys.stdout.write(data)
			else:
				msg = sys.stdin.readline()
				connection.send(f"{msg}".encode())
		#stdin = os.dup2(connection.fileno(),0)
		#stdout = os.dup2(connection.fileno(),1)
		


if __name__ == '__main__':
	main()