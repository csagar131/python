#importing sokcet module
import socket


ip = "0.0.0.0" # reciever ip address 
# we cant give a perticular ip address for receiver so 0.0.0.0 is by default 
port= 7777
# same as sender port number
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#creating a socket with ipv4      and UDP


#binding ip and port
s.bind((ip,port))

while True:
	msg=s.recvfrom(100)
	print(msg[0])
	s.sendto(("hello ip:"+(str)(msg[1][0])).encode('ascii'),msg[1])
