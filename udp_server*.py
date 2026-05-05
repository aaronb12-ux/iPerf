import socket
import time

HOST = "127.0.0.1"  #Standard loopback interface address (localhost)
PORT = 6000
BUFFER_SIZE = 8192 #number of bytes we receive in each call

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, 6000))

print(f"UDP server up and listening on {HOST} : {PORT}")

data, addr = s.recvfrom(8192)
start = time.perf_counter()
totalBytes = 0

while True:
    #waiting for incoming packets

    if data == b"__END__": #stop receiving
        break

    totalBytes += len(data)

    data, addr = s.recvfrom(8192)

end = time.perf_counter()
print(f"Bytes received: {totalBytes}")

totalTime = end - start
kb = totalBytes / 1024

throughput = kb / totalTime
backtoClient = f"Throughput: {throughput:.2f} KB/s"

s.sendto(backtoClient.encode(), addr)



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