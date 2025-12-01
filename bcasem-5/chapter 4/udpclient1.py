import socket

host = 'localhost'
port = 5000

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the address
s.bind((host, port))

# Set timeout BEFORE receiving
s.settimeout(5)

try:
    while True:
        msg, addr = s.recvfrom(1024)
        print('Received:', msg.decode())
except socket.timeout:
    print("Time is over and hence terminating...")

s.close()
