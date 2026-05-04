import socket

HOST = "127.0.0.1"
PORT = 6001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))


try:
    s.connect((HOST, PORT)) #connecting to the server
    s.sendall(b"Hello World") #sends data to the server
    data = s.recvfrom(1024) #reading servers reply
    
except Exception as e:
    print(f"Error: {e}")

print(f"Received {data!r}") #servers reply

