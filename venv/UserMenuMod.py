from Req_Mod import *
from DbMod import *
from encryption import *
from colorama import Fore, Back, Style

#Create user data
def cr_user(log,pswrd):
    user={'Login':log,'passowrd':pswrd}
    return user

def usrMenu(web):
    ans=input('Select User or Admin. ').upper()
    if ans=='A':
        print('Logged in successfully')
        #AdL, AdP=input('Please provide your login and password')

        Ops=input('Options: (I)nsertData,(S)electData ').upper()
        if Ops == 'S':
            selUsrData()


    elif ans == 'U':
        Uans =input('Are you a new user or do you want to login? New/Login ').upper()
        if Uans == 'N':
            # Insert data from user
            l, p = input('Please provide your login and password (separete with space): ').split()
            # encrypt(p)
            u = cr_user(l, p)
            addUser(web,u)
            insData(l,p)
            print('Please log into your new account.')
            usrMenu(web)
        elif Uans =='L':
            log,pswrd = input('Please provide Your login and password. ').split()
            checkLogIn(log,pswrd)
        else:
            pass
    else:
        pass
    usrMenu(web)
