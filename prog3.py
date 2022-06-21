import socket
import pickle as pk
import numpy as np
import time
import os

os.system("clear")
Host='' #CABEÇALHO DA TCP PARA RECEBIMENTO
Port=5000
tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Origem=(Host,Port)

def Juntar(Lista):  #FUNÇÃO PARA JUNTAR OS ITENS E DECODIFICAR
      Arquivo=pk.loads(b"".join(Lista))
      return Arquivo


tcp.bind(Origem) #RECEBE A INFORMAÇÃO DO PROG2
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
#      print("\nINVERSA: ",Arquivo[1])
      print("DETERMINANTE DA INVERSA: ",Arquivo[0])
      print("TEMPO DE ENVIO[microsegundo]: ",((time.time_ns()-Arquivo[1])/1000))
conn.close()
