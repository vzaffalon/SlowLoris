from socket import *

serverNameList = ['',"192.168.1.97","192.168.1.11"]
serverPort = 11750

for serverName in serverNameList:
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.settimeout(5)
        clientSocket.connect((serverName,serverPort))
        command = raw_input('Insira o comando para envio ao bots:')
        clientSocket.send(command)
        modifiedSentence = clientSocket.recv(1024)
        if modifiedSentence == "Confirmed":
            print 'Ataque iniciado'
        else:
            print "Comando invalido"
        clientSocket.close()
    except socket.error, exc:
        print "Nao foi possivel conectar com" + serverName
