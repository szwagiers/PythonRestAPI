from cryptography.fernet import Fernet
from colorama import Fore, Back, Style

def WrToBin(encspwrd):
    Bin = open("pswrdBin.bin","wb")
    Bin.write(key)
    Bin.close()


def encrypt(psw):
    key = Fernet.generate_key()
    KeyIns = Fernet(key)
    encP = KeyIns.encrypt(b'psw')
    #write key into a binary file
    WrToBin(key)


def decrypt(p):
    with open("pswrdBin.bin",'rb') as file_object:
        for line in file_object:
            if p==line:

