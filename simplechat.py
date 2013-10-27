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
	if checkForServer(IP,port):
		print "----Other client up."
		thread.start_new_thread(server, (port+1,))
		client(IP, port)
	else:
		print "----Other client not yet up."
		thread.start_new_thread(server, (port,))
		client(IP, port+1)


                        
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
		s.close
		return s.recv(1024)
	except:
		return "No response."
		


def client(ip, port):
	print "----Ready to send."
	while True:
		try:
			message = str(raw_input(""))
			sendMessage(port, ip, message)
		except:
			print '----Keyboard interupt. Quitting SimpleChat.'	
			break

def server(port):
	#socket stuff
	print "----Listening!"
	s = socket.socket()
	host = socket.gethostname()
	s.bind(('', port))
	s.listen(5)
	#where stuff happens
	while True:
		try:
			c, addr = s.accept()
			#print 'Got connection from', addr
			message = c.recv(1024)
			print "Partner>>", message
			c.send("boop")
			c.close()    
		except:
			print 'server error'	
			break





if __name__ == '__main__':
	dodisthang()    
