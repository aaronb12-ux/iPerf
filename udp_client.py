import socket

HOST = "127.0.0.1"
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Aaron is cooooooooll", (HOST, PORT))

data, addr = client.recvfrom(1024)

print(data.decode())