from Req_Mod import *
from DbMod import *
from encyption import *

#Create user data
def cr_user(log,pswrd):
    user={'Login':log,'passowrd':pswrd}
    return user

def usrMenu():
    ans=input('Select User or Admin. ').upper()
    if ans=='A':
        #AdL, AdP=input('Please provide your login and password')
        pass
    elif ans == 'U':
        Uans =input('Are You a new user or do You want to login? New/Login ').upper()
        if Uans == 'N':
            # Insert data from user
            l, p = input('Please provide your login and password (separete with space): ').split()
            encrypt(p)
            u = cr_user(l, p)
            addUser(u)
            insData(l,p)
        elif Uans =='L':
            log,pswrd = input('Please provide Your login and password. ').split()
            checkLogIn(log,pswrd)
        else:
            pass
    else:
        pass
    usrMenu()
