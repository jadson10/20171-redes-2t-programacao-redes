#!/usr/bin/python2.7

import socket


serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

opcao = raw_input("Escolha:\n 1-Somar\n 2-Raiz Quadrada\n 3-Sair\n")
clientSocket.sendto(opcao, (serverName, serverPort))

if opcao == '1':

    n1 = raw_input("digite n1 :")
    n2 = raw_input("digite n2 :")
    clientSocket.sendto(n1,(serverName, serverPort))
    clientSocket.sendto(n2,(serverName, serverPort))
    result2,serverAddress= clientSocket.recvfrom(2048)
    print("O resultado da soma eh ",result2)

elif opcao == '2':

       n1 = raw_input("digite n1 :")
       clientSocket.sendto(n1, (serverName, serverPort))
       result2, serverAddress = clientSocket.recvfrom(2048)
       print("A raiz quadrada do numero eh ", result2)

else:
       print("Mensagem invalida")

clientSocket.close()