from Req_Mod import *
from DbMod import *
#Create user data
def cr_user(n,s):
    user={'name':n,'surname':s}
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
            n, s = input('Please provide your data: ').split()
            u = cr_user(n, s)
            addUser(u)

        else:
            pass
    else:
        pass
