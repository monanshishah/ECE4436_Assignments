# UDPHeartbeatClient
# Import socket library
import socket
from socket import AF_INET, SOCK_DGRAM
# Import time
import time

serverName = '127.0.0.1'
serverPort = 12005
# Create a UDP socket for client
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
# Create a loop that sends messages to the server
count = 0
# Create time variable
currentTime = 0

while count < 10:
    currentTime = time.time()
    message = str(count) + " " + str(currentTime)
    clientSocket.sendto(message, (serverName, serverPort))
    count += 1
    print(message)
    time.sleep(1)

clientSocket.close()
