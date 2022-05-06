import socket
import struct

################### SERVER CONFIG ###################
localIP     = "127.0.0.1"
localPort   = 30001
bufferSize  = 1024
#####################################################

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams

while(True):

    receivedData = UDPServerSocket.recvfrom(bufferSize)
    bytesAddressPair = receivedData[0]
    client_status = receivedData[1]

    if(len(bytesAddressPair) > 20 ):
        
        gear = bytesAddressPair[25].to_bytes(1,'little')+bytesAddressPair[26].to_bytes(1,'little') + bytesAddressPair[27].to_bytes(1,'little') + bytesAddressPair[28].to_bytes(1,'little')
        gear = struct.unpack('i', gear)
        gear = gear[0]

        velocimetro = bytesAddressPair[33].to_bytes(1,'little')+bytesAddressPair[34].to_bytes(1,'little') + bytesAddressPair[35].to_bytes(1,'little') + bytesAddressPair[36].to_bytes(1,'little')
        velocimetro = struct.unpack('f', velocimetro)
        velocimetro = velocimetro[0]

        posX = bytesAddressPair[37].to_bytes(1,'little')+bytesAddressPair[38].to_bytes(1,'little') + bytesAddressPair[39].to_bytes(1,'little') + bytesAddressPair[40].to_bytes(1,'little')
        posX = struct.unpack('f', posX)
        posX = posX[0]

        rpm = bytesAddressPair[13].to_bytes(1,'little')+bytesAddressPair[14].to_bytes(1,'little') + bytesAddressPair[15].to_bytes(1,'little') + bytesAddressPair[16].to_bytes(1,'little')
        rpm = struct.unpack('i', rpm)
        rpm = rpm[0]

        print(posX)
        
    else:
        print("simulação parada")