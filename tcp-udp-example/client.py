#!/usr/bin/python

import socket
import sys

def sendOverTCP(host, port, inpt):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(inpt)

    while True:
        resp = s.recv(1024)

        if resp.isdigit():
	    print 'ANSWER: %d' %int(resp)
        else:
	    print 'Error: You must send a digit value.'

        s.close()
        exit(1)

def sendOverUDP(host, port, inpt):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(inpt, (host, port))
    resp, addr =s.recvfrom(1024)
    
    if resp.isdigit():
	print 'ANSWER: %d' %int(resp)
    else:
	print 'Error: You must send a digit value.'
    
    s.close()
    exit(1)

if len(sys.argv) < 5:
    print "Usage: ./client.py <protocol:tcp/udp> <hostname> <port> <value>"
    exit(0)

protocol = sys.argv[1]
host = sys.argv[2]
port = int(sys.argv[3])
inpt = sys.argv[4]

if protocol == 'tcp':
    sendOverTCP(host, port, inpt)
elif protocol == 'udp':
    sendOverUDP(host, port, inpt)
else:
    print "Wrong Protocol you must use tcp/udp as a protocol."
