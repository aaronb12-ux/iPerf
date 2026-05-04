import socket

HOST = "127.0.0.1"  #Standard loopback interface address (localhost)
PORT = 6000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, 6000))


print(f"UDP server up and listening on {HOST} : {PORT}")

while True:
    #waiting for incoming packets
    try:
        data, address = s.recvfrom(BUFFER_SIZE) #receiving data from the client
        message = data.decode()
        
        print(f"Received from {address}: {message}")

        s.sendto(b"ACK", address)

    except Exception as e:
        print("Error:", e)


'''
server counts all incoming bytes sent from the client. Count until the __END__ sentinel arrives
we then print the bytes recieved and the throughput

throughput = number_of_bytes_read / time_it_took_to_send_these_bytes


listen for bytes on ip: 127.0.0.1 and port: 6000


'''


'''
Building a UDP server using Python's socket API. The autograder will act as the client; it will send exactly 100 MB of data to the server, and the server must measure the throughput and report it back.
socket programming guide: https://realpython.com/python-sockets/
'''