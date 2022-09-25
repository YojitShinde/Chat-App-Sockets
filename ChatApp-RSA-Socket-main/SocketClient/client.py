import socket
# from Crypto.PublicKey import RSA
import socketrsa as sr

HOST = '172.16.64.26'
PORT = 7896
akhilKey = sr.akhilKey()
# print(type(akhilKey))
# print(akhilKey)
MartinPub, MartinPriv = sr.loadKeys()

#print(jaiPub,'\n',jaiPriv)
# print(jaiPub)
# print('====')
# print(jaiPriv)
# afinet ip version 4
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        text=input("Enter a message : ")
        ciphertext= sr.encrypt(text,akhilKey)
        #print(bytes(ciphertext))
        #mesg=sr.decrypt(ciphertext,MartinPriv)
        #print(mesg)
        s.sendall(ciphertext)
        akhilcipher = s.recv(1024)
        #akhilcipher = data
        #print(akhilcipher)
        akhilMesg = sr.decrypt(akhilcipher,MartinPriv)
        print('Received : ',akhilMesg)
        
# repr files to string