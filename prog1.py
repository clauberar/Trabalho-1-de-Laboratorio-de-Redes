import numpy as np
import pickle as pk
import socket
import os
import sys
import time

#ENDEREÇO DE IP E PORTA DA VM QUE VAI RECEBER  A MATRIZ
Host='192.168.125.11'
Port=5000
#CRIAÇÃO DA MATRIZ E PROTOCOLO DE ENVIO UDP
tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Dest=(Host,Port)

def criacao(Tamanho): #CRIAÇÃO DA MATRIZ E CONVERSÃO
        TempoInicio=time.time_ns()
        Matriz=np.random.randint(100,size=(Tamanho,Tamanho))
        print(Matriz)
        Arquivo=[Matriz,TempoInicio]
        Arquivo=pk.dumps(Arquivo)
        return Arquivo

def divisao(Arquivo,Lista):
        i=0
        ArquivoBytes=sys.getsizeof(Arquivo) #Tamanho em bytes do Arquivo
        ArquivoDiv=int(np.ceil(ArquivoBytes/1024))  #A quantidade de frame que vai ser necessário
        FrameTam=int(len(Arquivo)/ArquivoDiv) #O tamanho do  frame (não é bytes)
        FrameBytes=sys.getsizeof(Arquivo[:FrameTam]) #O tamnho do frame em bytes

        while FrameBytes>1024:  #Garantir que o frame vai ter no máximo 1024bytes
              ArquivoDiv+=2
              FrameTam=int(len(Arquivo)/ArquivoDiv)
              FrameBytes=sys.getsizeof(Arquivo[:FrameTam])

        for i in range(ArquivoDiv):  #criando uma lista com os frames
             Frame=Arquivo[(i)*FrameTam:(i+1)*FrameTam]
             Lista.append(Frame)

             if i==(ArquivoDiv-1) and (i+1)*FrameTam<len(Arquivo): #Garantir que tudo esta dentro da lista
                Frame=Arquivo[(i+1)*FrameTam:]
                Lista.append(Frame)
        return Lista

def envio(Lista): #envio de cada itens da lista
         for i in Lista:
            tcp.sendall(i)
         time.sleep(0.1)
         tcp.sendall(pk.dumps("fim"))

#MAIN
tcp.connect(Dest)
opcao="S"

while opcao=="S":
   Tamanho=int(input("\nTAMANHO DA MATRIZ QUADRADA:"))
   Quantidade=int(input("QUANTIDADE DE MATRIZES A SEREM CRIADAS:"))

   for i in range(Quantidade):
      Lista=[]
      Arquivo=criacao(Tamanho)  #Chamando a função criacao para criar a matriz e converter

      if sys.getsizeof(Arquivo)>1024:  #verificação do tamanho para ver se vai preciso dividir
         Lista=divisao(Arquivo,Lista)
         envio(Lista)  #Chamando a função envio para enviar a lista com o(s) frame(s)
      else:
         Lista.append(Arquivo)
         envio(Lista)  #Chamando a função envio para enviar a lista com o(s) frame(s)

   time.sleep(0.2)
   opcao=input("DESEJA ENVIAR MAIS MATRIZ[S/N]").upper()

