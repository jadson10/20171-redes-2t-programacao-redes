#!/usr/bin/python2.7

import socket
from math import sqrt

serverHost = 'localhost'
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

print("Servidor pronto para receber: ")

while True:

    opcao, clientAddress = serverSocket.recvfrom(2048)

    def soma():

     n1,clientAddress = serverSocket.recvfrom(2048)
     n2,clientAddress = serverSocket.recvfrom(2048)
     result2 = int(n1)+int(n2)
     print("O resultado da soma eh ", result2)
     serverSocket.sendto(str(result2),clientAddress)


    def raiz_quadrada():

      n1, clientAddress = serverSocket.recvfrom(2048)
      result2 = sqrt(float(n1))
      print("A raiz quadrada do numero eh ", result2)
      serverSocket.sendto(str(result2), clientAddress)

    def mensagem():

      print("Mensagem invalida")


    if opcao == '1':
      print("chamando soma")
      soma()

    elif opcao == '2':
      print("chamando funcao raiz")
      raiz_quadrada()

    else:
      mensagem()

serverSocket.close()







