import os
import socket
os.system("cls")
hostname = input("Enter Domain Name :")
print("ip adr: " + socket.gethostbyname(hostname))
