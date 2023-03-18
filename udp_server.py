import socket
import pickle
import AsynEncryption
import math

encryptionKeys = AsynEncryption.generateKeys()
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 4096
msgFromServer       = "Hello UDP Client"
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
clientKey = None
decryptedMessage = None
# Listen for incoming datagrams
while(clientKey == None):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    #clientMsg = str(message,"utf-8")
    message1, publicKey = pickle.loads(message)
    clientIP  = "Client IP Address:{}".format(address)
    print('Messagem from client: ',message1)
    # Sending a reply to client
    bytesToSend = pickle.dumps((msgFromServer, encryptionKeys[1]))
    UDPServerSocket.sendto(bytesToSend, address)
    clientKey = publicKey

while (clientKey != None and decryptedMessage != 'exit'):
    clientData, clientAddress = UDPServerSocket.recvfrom(bufferSize)

    #clientMsg = str(message,"utf-8")
    #message2, publicKey = pickle.loads(clientData)
    cryptedMessage = int.from_bytes(clientData, byteorder='big')
    decryptedMessage = AsynEncryption.decryptMessage(cryptedMessage, encryptionKeys[0])
    clientIP  = "Client IP Address:{}".format(clientAddress)
    print('')
    print('Crypted Message from client: ',cryptedMessage)
    print('')
    print('Decrypted Message from client: ',decryptedMessage)
    print(clientIP)
    # Sending a reply to client


    encryptedMessage = AsynEncryption.encryptMessage(msgFromServer, clientKey)
    numberOfBytes = math.ceil(encryptedMessage.bit_length()/8)
    bytesToSend         = encryptedMessage.to_bytes(numberOfBytes, byteorder='big')
    #data = pickle.dumps((bytesToSend, publicKey))

    # Send to server using created UDP socket
    UDPServerSocket.sendto(bytesToSend, address)
    #bytesToSend = pickle.dumps((msgFromServer, encryptionKeys[1]))
    #UDPServerSocket.sendto(bytesToSend, address)
