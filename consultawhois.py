#!/usr/share/python

import socket
import sys

dominio = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send((dominio + "\n").encode('utf-8'))
resposta = s.recv(1024).split()
whois = (resposta[19])

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois,43))
s1.send((dominio + "\n").encode('utf-8'))
resp = s.recv(2048).decode('utf-8', 'ignore')


print (resp)
