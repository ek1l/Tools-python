import socket,sys,os

os.system('clear')

host = sys.argv[1]

print(f"{host} , ----> , {socket.gethostbyname(host)} ")