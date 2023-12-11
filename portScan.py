 
import socket
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("whois.iana.org", 43))

s.send((sys.argv[1] + "\r\n").encode())

resposta = s.recv(1024)



if os.path.exists('consultaIana.txt'):
    os.remove('consultaIana.txt')

with open('consultaIana.txt', 'w') as arquivo:
    arquivo.write(resposta.decode().replace('\\r\\n', '\n'))

def search_refer(arquivo):
    referencias = []
    with open(arquivo, 'r') as arquivo_texto:
        for linha in arquivo_texto:
            if 'refer:' in linha:
                referencias.append(linha.split('refer:')[1].strip())
    return referencias

nome_do_arquivo = 'consultaIana.txt'
referencias_encontradas = search_refer(nome_do_arquivo)

if referencias_encontradas:
    print(f"A referência '{referencias_encontradas}' foi encontrada, buscando novas informações...")

    for refer in referencias_encontradas:
        print(refer)
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect((refer, 43))
        s1.send((sys.argv[1] + "\r\n").encode())
        res = s1.recv(1024)
        print(res.decode('utf-8','ignore').replace("\\r\\n", "\n"))
        nome_arquivo_segunda_requisicao = f'requisicao_{refer}.txt'
        with open(nome_arquivo_segunda_requisicao, 'w') as arquivo_segunda_requisicao:
            arquivo_segunda_requisicao.write(res.decode('utf-8','ignore').replace("\\r\\n", "\n"))

 
        s1.close()
else:
    print('Refer não encontrada')
    s.close()			
 
s.close()
