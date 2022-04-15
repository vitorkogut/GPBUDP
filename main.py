import socket


localIP     = "127.0.0.1"
localPort   = 30001
bufferSize  = 1024


msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")
# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    print(bytesAddressPair)