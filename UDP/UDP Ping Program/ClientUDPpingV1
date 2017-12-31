from socket import *
from datetime import datetime
import statistics


serverName = '127.0.0.1'
serverPort = 12000
Requests = 200
clientSocket = socket(AF_INET, SOCK_DGRAM)  # created a client side socket
clientSocket.settimeout(2)  # set the timeout at 2 seconds

counter = 0  # variable that tracks the sequence number
min = 0.0
avg = 0.0
max = 0.0
loss = 0  # variable that tracks the number of loss packets
responseTimes = []

while counter < Requests:
    message = "Ping: "
    currentTime = datetime.now()  # assign current time to a variable
    try:
        message = message + str(counter) + ' -> ' + str(datetime.now())
        elapsed = (datetime.now() - currentTime).microseconds / 1000

        responseTimes.append(elapsed)

        # Calculate the average, min and max
        avg += elapsed
        if counter == 0:
            min = elapsed
            max = elapsed
        else:
            if min > elapsed:
                min = elapsed
            else:
                if max < elapsed:
                    max = elapsed
        counter += 1

        clientSocket.sendto(bytes(message, "UTF-8"), (serverName, serverPort))

        # receives msg from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        print(modifiedMessage)

    except timeout:
        loss += 1
        print('Request Timed Out')

avg = avg / (Requests - loss)
lossPercent = loss/Requests * 100
stddev = statistics.stdev(responseTimes)

print('RTT Min: ' + str(min) + ' ms')
print('RTT Avg: ' + str(avg) + ' ms')
print('RTT Max: ' + str(max) + ' ms')
print('Packet Loss:' + str(lossPercent) + '%')
print('Standard Deviation: ' + str(stddev))

clientSocket.close()
