#!/usr/bin/python

import socket
import os
import md5
import sys

UDP_IP = 'localhost'
UDP_PORT = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def isFile(filename):
    return os.path.isfile(filename)

def rrq(data, sock, addr):
    print "RRQ: addr:%s, data:%s" %(addr, data)
    msg = ''
    f = data.split()[1]
    if isFile(f):
        msg = 'ACK ' + f
    else:
        msg = 'NACK ' + f
    sock.sendto(msg, addr)

def irq(data, sock, addr):
    print "IRQ: addr:%s, data:%s" %(addr, data)
    msg = ''
    f_name = data.split()[1]
    f = open(f_name)
    m = md5.new(f.read()).hexdigest()

    if isFile(f_name):
        msg = 'IACK %s %s %s' %(f_name ,os.path.getsize(f_name), m)
    else:
        msg = 'INACK %s' %(f_name)
    sock.sendto(msg, addr)

def grq(data, sock, addr):
    print "GRQ: addr:%s, data:%s" %(addr, data)
    msg = ''
    f_name = data.split()[1]
    msg = 'BEGIN %s' %(f_name)
    sock.sendto(msg, addr)
    dpk(data, sock, addr, f_name)

def dpk(data, sock, addr, filename):
    server_count = int(data.split()[2])
    server_number = int(data.split()[3])
    with open(filename, 'rb') as f:
        count = 1
        segment_count = 0
        while True:
            segment_count += 1
            chunk = f.read(100)
            if not chunk:
                break
            msg = "DATA %s %s |%s" %(filename, segment_count, chunk)
            if server_number == count:
                sock.sendto(msg, addr)
                count += 1
            else:
                count += 1
            if server_count < count:
                count = 1
    sock.sendto('DONE', addr)

while True:
    data, addr = sock.recvfrom(1024)
    command = data.split()[0]
    if command == 'READ':
        rrq(data, sock, addr)
    elif command == 'INFO':
        irq(data, sock, addr)
    elif command == 'GET':
        grq(data, sock, addr)
