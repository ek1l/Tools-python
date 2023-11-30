#!/usr/bin/python
import socket, os

os.system('clear')
print("Interagindo com FTP SERVER")

ip = str(input("Digite o IP: ")).strip()
porta = 21

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip, porta))
banner = meusocket.recv(1024)
print(banner.decode('utf-8'))

print("Enviando usuário")
meusocket.send(b"USER ricardo\n")
banner = meusocket.recv(1024)
print(banner.decode('utf-8'))

print("Enviando password")
meusocket.send(b"PASS ricardo\n")
banner = meusocket.recv(1024)
print(banner.decode('utf-8'))
