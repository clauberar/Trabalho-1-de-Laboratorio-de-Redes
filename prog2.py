import socket
import pickle as pk
import numpy as np
import os
import time
import sys

os.system("clear") 

Host='' #CABEÇALHO DA TCP PARA RECEBIMENTO
Port=5000
tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Origem=(Host,Port)

HostProx='192.168.125.73' #CABEÇALHO DA TCP PARA ENVIAR
PortProx=5000
tcpProx=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
DestProx=(HostProx,PortProx)

def Juntar(Lista):  #FUNÇÃO PARA JUNTAR OS ITENS E DECODIFICAR
    Arquivo=pk.loads(b"".join(Lista))
    print(Arquivo)
    return Arquivo

def envio(ArquivoProx): #envio de cada itens da lista
         tcpProx.sendall(ArquivoProx)
         time.sleep(0.1) 
         tcpProx.sendall(pk.dumps("fim"))
         print("enviado")

tcp.bind(Origem) #RECEBE A INFORMAÇÃO DO PROG1
tcpProx.connect(DestProx) #ABRINDO CONEXÃO COM O PRÓXIMO
tcp.listen(1)
conn,addr=tcp.accept()
print("conectado:", addr)
Lista=[]
while True:
    Frame= conn.recv(1024)
    Lista.append(Frame)
    if Lista[-1]==b'\x80\x04\x95\x07\x00\x00\x00\x00\x00\x00\x00\x8c\x03fim\x94.':
        Lista.pop(-1)
        Arquivo=Juntar(Lista)
        Inversa=np.linalg.inv(Arquivo[0]) #INVERTER A MATRIZ
        Determinante=np.linalg.det(Inversa) #DIAGOANAL DA MATRIZ INVERTIDA
        ArquivoProx=[Determinante,Arquivo[1]] #LISTA PARA ENVIAR PARA O PROG3
        ArquivoProx=pk.dumps(ArquivoProx) #CONVERTENDO A LISTA
        Lista=[]
        time.sleep(0.01)
#ENVIANDO
        envio(ArquivoProx)  #Chamando a função envio para enviar a lista com o(s) frame(s)
#conn.close()
