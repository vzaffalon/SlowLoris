from socket import *
serverName = ''
serverPort = 11997
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
command = raw_input('Insira o comando para envio ao bots:')
clientSocket.send(command)
modifiedSentence = clientSocket.recv(1024)
if modifiedSentence == "Confirmed":
    print 'Ataque iniciado'
else:
    print "Comando invalido"
clientSocket.close()
