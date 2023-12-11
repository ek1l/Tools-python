import socket,sys,os

host = sys.argv[1]

print(f"{host} , ----> , {socket.gethostbyname(host)} ")