import socket

s = socket.socket()

port = 8000

s.connect(('192.168.8.184', port))

data = s.recv(1024)

s.send(b'Hi, Im your client');

print (data)

s.close()
