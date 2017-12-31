# Import socket library
import socket
from socket import AF_INET, SOCK_DGRAM
# Import sys for exit

# Import time
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
serverSocket.settimeout(1)
# Assign IP address and port number to socket
serverSocket.bind(('', 12005))
lostPacketCount = 0
listen = True
while listen == True:

    try:  # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        lostPacketCount = 0
        travelTime = message[2:]
        currentTime = time.time()
        print(float(currentTime) - float(travelTime))

    except socket.timeout:
        print("Packet Lost")
        lostPacketCount += 1

    if lostPacketCount > 5:
        listen = False

print("We can assume the application stopped transmitting")
serverSocket.close()
