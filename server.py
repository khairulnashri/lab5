import socket

s = socket.socket()
print("Berjaya buat sokett")

port = 8000

s.bind(('', port))
print("Successfully bind at port: " + str(port))

s.listen(5)
print("Waiting for client...")

while True:
        c, addr = s.accept()
        print("Connection from: " + str(addr))

        c.send(b'Terima Kasih!')
        buffer = c.recv(1024)
        print(buffer)
c.close()

