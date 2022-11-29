import threading,time,socket


def main():

	dataReceived = "None"
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	sock.bind(("127.0.0.1",8080))
	sock.listen()
	sock.accept()
	dataReceived =  threading.Thread(task=sock.recv(3000).decode('utf-8'))
	time.sleep(5)
	print(dataReceived)

if __name__ == '__main__':
	main()