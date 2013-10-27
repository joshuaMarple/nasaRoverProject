#!/usr/bin/env python
import sys
import socket
import thread
import time


######## Main loop. ########

def dodisthang():
	# try:
	print "SimpleChat starting."
	port = int(raw_input("port:"))
	server(port)


                        
#### Other functions go here.######



def server(port):
	#socket stuff
	print "Server up!"
	s = socket.socket()
	host = socket.gethostname()
	s.bind(('', port))
	s.listen(5)
	#where stuff happens
	while True:
		try:
			c, addr = s.accept()
			print 'Got connection from', addr
			message = c.recv(1024)
			print "Partner>>", message
			c.send("boop")
			c.close()    
		except:
			print 'unknown error'	
			break




if __name__ == '__main__':
	dodisthang()    
