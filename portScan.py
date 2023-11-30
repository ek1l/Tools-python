import socket
import concurrent.futures
import os
import sys

def verifica_porta(porta):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(1)   

    if meusocket.connect_ex((sys.argv[1], porta)) == 0:
        print(f"Porta {porta} [ABERTA]")

    meusocket.close()

def main():
    os.system("clear")

 
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        portas = range(1, 65000)
        executor.map(verifica_porta, portas)

if __name__ == "__main__":
    main()
