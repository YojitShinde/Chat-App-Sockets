import socket
import rsa
import socketrsa as sr
HOST = '192.168.1.21'
PORT = 8989
# def jaiKey():
#     with open('jaiPub.pem', 'rb') as p:
#         publicKey = rsa.PublicKey.load_pkcs1(p.read())
#     with open('jaiPriv.pem', 'rb') as p:
#         privateKey = rsa.PrivateKey.load_pkcs1(p.read())
#     return publicKey, privateKey
# # sr.generateKeys()
yojitPub , yojitPriv = sr.loadKeys()
swenPub = sr.swenKey()
# type(jaiPub)
# print(jaiPub,'/n',jaiPriv)
#akhilPub, akhilPriv = sr.loadKeys()
#print(akhilPub)
# publicKey, privateKey = sr.loadKeys()
def conn_chat(a):
    conn, addr = a.accept()
    print('Connected by', addr)
    while True:
            swenCipher = conn.recv(1024)
            #print("Received:",jaiRec)
            swenMesg = rsa.decrypt(swenCipher, yojitPriv).decode('utf-8')
            print("Received",swenMesg)
            text = input("Send a message: ")
            ciphertext = rsa.encrypt(text.encode('utf-8'), swenPub)
            #print(bytes(ciphertext))
            #mesg=rsa.decrypt(ciphertext,jaiPriv).decode('utf-8')
            #print(mesg)
            conn.sendall(ciphertext)
       

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn_chat(s)