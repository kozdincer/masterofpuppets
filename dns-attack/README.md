Create and Send DNS package
===========================
This script change source ip address and lookup a DNS query.

* You have to install python-scapy.
* You have to run this script with root privileges.

**Example:** sudo /usr/bin/python sendDNSpackage.py

### Example Usage & Output


`$ sudo py sendDNSRequest.py`

`What is your DNS server which you want to resolve from? :: 192.168.1.111`

`What is your source ip address which you want to send DNS request from? :: 192.168.1.155`

`What is the address which will be queried by DNS server? :: my.domain.com`



`Information`

`===========`

`Source IP     : 192.168.1.155`

`Destination IP: 192.168.1.111`

`DNS Query     : my.domain.com`



`Package details`

`===============`



`###[ IP ]###`

`  version   = 4`

`  ihl       = None`

`  tos       = 0x0`

`  len       = None`

`  id        = 1`

`  flags     = `

`  frag      = 0`

`  ttl       = 64`

`  proto     = ip`

`  chksum    = None`

`  src       = 192.168.1.155`

`  dst       = 192.168.1.111`

`  \options   \`

`None`

``

`###[ UDP ]###`

`  sport     = domain`

`  dport     = domain`

`  len       = None`

`  chksum    = None`

`None`

``

`###[ DNS ]###`

`  id        = 0`

`  qr        = 0`

`  opcode    = QUERY`

`  aa        = 0`

`  tc        = 0`

`  rd        = 1`

`  ra        = 0`

`  z         = 0`

`  rcode     = ok`

`  qdcount   = 1`

`  ancount   = 0`

`  nscount   = 0`

`  arcount   = 0`

`  \qd        \`

`   |###[ DNS Question Record ]###`

`   |  qname     = 'my.domain.com'`

`   |  qtype     = A`

`   |  qclass    = IN`

`  an        = None`

`  ns        = None`

`  ar        = None`

`None`

``

`Is it OK? (Y/n)`

`.`

`Sent 1 packets.`

``
