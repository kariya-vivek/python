import socket

host = 'localhost'
port = 6767

s = socket.socket()
s.bind((host, port))
s.listen(1)
c, addr = s.accept()
print("A client accepted connection")

fname = c.recv(1024)
fname = str(fname.decode())
print("File name received from client: " + fname)

try:
    f = open(fname, 'rb')
    content = f.read()
    c.send(content)
    print("File content send to client")
    f.close()
except FileNotFoundError:
    c.send(b'File does not exist')

c.close()
