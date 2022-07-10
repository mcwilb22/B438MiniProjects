import time
import sys
from socket import *

# Creating a UDP socket.
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Creating a timeout for 1 second.
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddr = (sys.argv[1], int(sys.argv[2]))

# Ping ten times
for i in range(10):
    
    sendTime = time.time()
    message = 'Ping ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message, remoteAddr)
    
    try:
        data, server = clientSocket.recvfrom(1024)
        recdTime = time.time()
        rtt = recdTime - sendTime
        print('Message Received '), data
        print('Round Trip Time '), rtt
        print
    
    except timeout:
        print('REQUEST TIMED OUT')
        print
