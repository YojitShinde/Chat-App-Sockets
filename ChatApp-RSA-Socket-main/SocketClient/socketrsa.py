import rsa as rs

def generateKeys():
    (publicKey, privateKey) = rs.newkeys(1024)
    with open("Client_Keys/SwenPub.pem", "wb") as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open("Client_Keys/SwenPriv.pem", "wb") as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open("Client_Keys/SwenPub.pem", "rb") as p:
        publicKey = rs.PublicKey.load_pkcs1(p.read())
    with open("Client_Keys/SwenPriv.pem", "rb") as p:
        privateKey = rs.PrivateKey.load_pkcs1(p.read())
    return publicKey,privateKey

def encrypt(message, key):
    return rs.encrypt(message.encode('utf-8'), key)

def decrypt(ciphertext, key):
    return rs.decrypt(ciphertext, key).decode('utf-8')
    
def sign(message, key):
    return rs.sign(message.encode('utf-8'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rs.verify(message.encode(''), signature, key,) == 'SHA-1'
    except:
        return False

def yojitKey():
    with open("Client_Keys/YojitPub.pem", "rb") as p:
        yojit = rs.PublicKey.load_pkcs1(p.read())
    return yojit
    
# generateKeys()
# publicKey, privateKey = loadKeys()

# message = input('Write your message here:')
# ciphertext = encrypt(message, publicKey)

# signature = sign(message, privateKey)

# text = decrypt(ciphertext, privateKey)

# print(f'Cipher text: {ciphertext}')
# print(f'Signature: {signature}')

# if verify(text, signature, publicKey):
#     print('Successfully verified signature')
# else:
#     print('The message signature could not be verified')
