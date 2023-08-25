from socket import *

serverName = "192.168.15.8"  # Server's IP address
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket

def encrypt(texto_plano, key=4):
    '''(Caesar, str, int) -> str
    Returns the texto_plano encrypted using the Caesar cipher
    with the given key (default is 4).
    '''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_text = ''
    texto_plano = texto_plano.upper()
    for ch in texto_plano:
        if ch in letters:
            idx = letters.find(ch) + key
            if idx >= 26:
                idx -= 26
            cipher_text += letters[idx]
    return cipher_text

print("UDP Client\n")
while True:
    message = input("Input message: ")

    if message == "exit":
        break

    encryptedMessage = encrypt(message)
    clientSocket.sendto(bytes(encryptedMessage, "utf-8"), (serverName, serverPort))

clientSocket.close()
