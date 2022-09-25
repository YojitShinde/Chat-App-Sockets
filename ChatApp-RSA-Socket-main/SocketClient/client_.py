import socket

import socketrsa as sr

HOST = '192.168.1.21'
PORT = 8989
yojitKey = sr.yojitKey()


publickey, privateKey = sr.loadKeys()
# afinet ip version 4
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        text=input("Enter a message: ")
        ciphertext= sr.encrypt(text,yojitKey)
        s.sendall(ciphertext)
        data = s.recv(1024)
        #yojitcipher = data.decode("ascii")
        yojitMesg = sr.decrypt(data,privateKey)
        print('Receive',yojitMesg)
# repr files to string