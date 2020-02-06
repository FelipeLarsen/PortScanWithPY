#!/usr/bin/python

import socket, sys

for port in range(1,65535):
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sockets.connect_ex((sys.argv[1], port)) == 0:
  print "Porta", port," - status [ABERTA]"
  sockets.close() 
