#!/usr/share/python
import socket,sys

sys('clear')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send((sys.argv[1] + "\r\n").encode())
resposta = s.recv(1024)
print(resposta)