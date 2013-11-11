#!/usr/bin/python
import socket
import sys
import thread
import time

def sendMessage(sock, ip, port, msg):
    sock.sendto(msg, (ip, port))

def sendRead(ip, port, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "READ " + filename
    sendMessage(sock, ip, port, msg)
    buf = sock.recvfrom(1024)[0]
    #if buf.split()[0] == 'ACK':
        #print buf

def sendInfo(ip, port, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "INFO " + filename
    sendMessage(sock, ip, port, msg)
    buf = sock.recvfrom(1024)[0]
    #print buf

def sendGet(ip, port, filename, server_count, server_number):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "GET %s %d %d" %(filename, server_count, server_number)
    sendMessage(sock, ip, port, msg)
    buf = sock.recvfrom(1024)[0]
    while True:
        data, addr = sock.recvfrom(1024)
        #if data.split()[0] == 'BEGIN':
            #print data
        if data.split()[0] == 'DATA':
            start = data.index('|') + 1
            d = data[start:]
            print d
        elif data.split()[0] == 'DONE':
            #print 'Download completed...'
            break

args = sys.argv
file_name = args[1]
servers = args[2:]

server_number = 1
for server in servers:
    d_ip = server.split(":")[0]
    d_port = server.split(":")[1]

    # Check reads.
    thread.start_new_thread(sendRead, (d_ip, int(d_port), file_name))
    time.sleep(1)

    # Get infos.
    thread.start_new_thread(sendInfo, (d_ip, int(d_port), file_name))
    time.sleep(1)

    # Get data.
    thread.start_new_thread(sendGet, (d_ip, int(d_port), file_name, len(servers), server_number))
    time.sleep(1)
    server_number += 1

exit(1)
