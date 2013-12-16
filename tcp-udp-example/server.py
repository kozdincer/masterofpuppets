#!/usr/bin/python

import socket
import sys
import time
from threading import Thread

def serverTCP(host, port):
    print "Starting TCP Server..."
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        resp = (conn.recv(1024)).strip()
	print 'TCP Received: %s' %resp

        if resp.isdigit():
	    conn.send('%d' %int(resp)*4)
        else:
	    conn.send('No')

def serverUDP(host, port):
    print "Starting UDP Server..."
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    while True:
	resp, addr = s.recvfrom(1024)
	print "UDP Received: %s" %resp

	if resp.isdigit():
	    s.sendto(digitOfPi(int(resp)), addr)
	else:
	    s.sentto('No', addr)

def digitOfPi(digit):
    pi_digits = "141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609"
    return pi_digits[:digit]

if len(sys.argv) < 3:
    print "Usage: ./server.py <hostname> <port_number>"
    exit(0)

host = sys.argv[1]
port = int(sys.argv[2])
tcp_t = Thread(target=serverTCP, args=(host,port))
udp_t = Thread(target=serverUDP, args=(host,port))

tcp_t.start()
udp_t.start()
