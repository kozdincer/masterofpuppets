#/usr/bin/python

from scapy.all import IP, UDP, DNS, DNSQR, send

# Get all input about DNS package.
destination_input = str(raw_input('What is your DNS server which you want to resolve from? :: '))
source_input = str(raw_input('What is your source ip address which you want to send DNS request from? :: '))
query_input = str(raw_input('What is the address which will be queried by DNS server? :: '))

# Create ip, udp and dns packages.
i = IP(dst=destination_input)
i.src = source_input
u = UDP(dport=53)
d = DNS(rd=1,qd=DNSQR(qname=query_input))

# Print all information.
print ""
print "Information"
print "==========="
print "Source IP     : %s" %source_input
print "Destination IP: %s" %destination_input
print "DNS Query     : %s" %query_input
print ""
print "Package details"
print "==============="
print ""
print i.show()
print ""
print u.show()
print ""
print d.show()
print ""

# Confirmation.
is_ok = raw_input("Is it OK? (Y/n)")

# Send or exit.
if is_ok == "y" or is_ok == "Y" or is_ok == "":
    p = send(i/u/d)
else:
    print "Bye."

