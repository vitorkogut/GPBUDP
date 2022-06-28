import socket
import struct
import tkinter as tk
import tk_tools as tkt

################### SERVER CONFIG ###################
localIP     = "127.0.0.1"
localPort   = 30001
bufferSize  = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
#####################################################


################ DATA CONTROL ################
enable_rpm = True
enable_gear = False
enable_velocimetro = False
enable_posX = False
enable_Yaw = True
enable_Pitch = True
enable_Roll = True

enable_GUI = True
data_output = {}
##############################################


################ GUI CONFIG ##################
if enable_GUI:
    window = tk.Tk()
    window.title("GP BIKES DATA")
    window.geometry('900x800')
    side_view = tk.PhotoImage(file="sideView.png")
    back_view = tk.PhotoImage(file="backView.png")
    side_view_label = tk.Label(image=side_view)
    side_view_label.grid(column=0,row=0,sticky="NESW")
    back_view_label = tk.Label(image=back_view)
    back_view_label.grid(column=0,row=1,sticky="NESW")
    roll_label = tk.Label(text="ND")
    roll_label.configure(font=("Arial",75))
    roll_label.grid(column=1,row=1)
    pitch_label = tk.Label(text="ND")
    pitch_label.configure(font=("Arial",75))
    pitch_label.grid(column=1,row=0)
    RPM_gauge = tkt.RotaryScale(window,max_value=16000,unit="RPM",size=200,needle_thickness=8)
    RPM_gauge.grid(column=2,row=0)
    
##############################################


while(True): # main loop server
    receivedData = UDPServerSocket.recvfrom(bufferSize)
    bytesAddressPair = receivedData[0]
    client_status = receivedData[1]

    if(len(bytesAddressPair) > 20 ):
        if enable_rpm:
            rpm = bytesAddressPair[13].to_bytes(1,'little')+bytesAddressPair[14].to_bytes(1,'little') + bytesAddressPair[15].to_bytes(1,'little') + bytesAddressPair[16].to_bytes(1,'little')
            rpm = struct.unpack('i', rpm)
            rpm = rpm[0]
            data_output["rpm"] = rpm
        
        if enable_gear:
            gear = bytesAddressPair[25].to_bytes(1,'little')+bytesAddressPair[26].to_bytes(1,'little') + bytesAddressPair[27].to_bytes(1,'little') + bytesAddressPair[28].to_bytes(1,'little')
            gear = struct.unpack('i', gear)
            gear = gear[0]
            data_output["gear"] = gear

        if enable_velocimetro:
            velocimetro = bytesAddressPair[33].to_bytes(1,'little')+bytesAddressPair[34].to_bytes(1,'little') + bytesAddressPair[35].to_bytes(1,'little') + bytesAddressPair[36].to_bytes(1,'little')
            velocimetro = struct.unpack('f', velocimetro)
            velocimetro = float(velocimetro[0]) * 3.6
            data_output["velocimetro"] = velocimetro

        if enable_posX:
            posX = bytesAddressPair[37].to_bytes(1,'little')+bytesAddressPair[38].to_bytes(1,'little') + bytesAddressPair[39].to_bytes(1,'little') + bytesAddressPair[40].to_bytes(1,'little')
            posX = struct.unpack('f', posX)
            posX = posX[0]
            data_output["posX"] = posX

        if enable_Yaw:
            yaw = bytesAddressPair[109].to_bytes(1,'little')+bytesAddressPair[110].to_bytes(1,'little') + bytesAddressPair[111].to_bytes(1,'little') + bytesAddressPair[112].to_bytes(1,'little')
            yaw = struct.unpack('f', yaw)
            yaw = yaw[0]
            data_output["yaw"] = yaw
        
        if enable_Pitch:
            pitch = bytesAddressPair[113].to_bytes(1,'little')+bytesAddressPair[114].to_bytes(1,'little') + bytesAddressPair[115].to_bytes(1,'little') + bytesAddressPair[116].to_bytes(1,'little')
            pitch = struct.unpack('f', pitch)
            pitch = pitch[0]
            data_output["pitch"] = pitch

        if enable_Roll:
            roll = bytesAddressPair[117].to_bytes(1,'little')+bytesAddressPair[118].to_bytes(1,'little') + bytesAddressPair[119].to_bytes(1,'little') + bytesAddressPair[120].to_bytes(1,'little')
            roll = struct.unpack('f', roll)
            roll = roll[0]
            data_output["roll"] = roll

        if enable_GUI:
            roll_label['text'] = "{:.2f}".format(data_output['roll'])
            pitch_label['text'] = "{:.2f}".format(data_output['pitch'])
            RPM_gauge.set_value(data_output['rpm'])
            window.update()
            
        
    else:
        print("simulação parada")

