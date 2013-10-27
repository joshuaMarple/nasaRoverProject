#!/usr/bin/env python
import sys
import socket
import thread
import time


######## Main loop. ########

def dodisthang():
	# try:
	print "SimpleChat starting."
	IP = str(raw_input("IP:"))
	port = int(raw_input("port:"))
	print checkForServer(IP,port)
	client(IP,port)


                        
#### Other functions go here.######
def checkForServer(IP, port):
	if sendMessage(port, IP, "foo") == "boop":
		return True
	else: 
		return False

def sendMessage(port, ip, message):
	try:
		#setup
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
		if message == '':
			message = 'Blank Message.'           
		s.connect((ip, port))
		s.sendall(message)
		data =  s.recv(1024)
		s.close
		return data
	except:
		print "No response."
		return "fish"


def client(ip, port):
	while True:
		try:
			print "Client up."
			message = str(raw_input(">>:"))
			sendMessage(port, ip, message)
		except:
			print 'unknown error'	
			break




if __name__ == '__main__':
	dodisthang()    
