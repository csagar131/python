#!/usr/bin/python3

#importing the socket module
import socket

#creating a socket ip:port
               
                    #ipv4          #UserDatagramProtocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# receiver ip address
ip="13.233.36.255"      #please replace with your receiver ip addr

#receiver port address
port=7777

#for repeated communication
while True:
    msg=input("Enter your message:----->>>> ")  #message from sender side
    n=msg.encode('ascii')        #encoding the message like one-to-one encryption
    s.sendto(n,(ip,port))    #sending the message n to destined (ip,port)
    rmsg=s.recvfrom(100)  #acknoledgement from the reciever side
    print(rmsg)


