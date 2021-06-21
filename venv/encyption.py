from cryptography.fernet import Fernet



def encrypt(psw):
    key = Fernet.generate_key()
    KeyIns = Fernet(key)
    encP = KeyIns.encrypt(b'psw')
    return key,encP

#def decrypt(p):
