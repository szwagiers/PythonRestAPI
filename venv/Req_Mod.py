from DbMod import *
import requests
from colorama import Fore, Back, Style
web='http://localhost:3000'

#print response with status code
def ConCheck(w):
    response = requests.get(w)
    if response.status_code == 200 :
        print(Fore.GREEN, 'Status code:' + str(response.status_code))
        print(Style.RESET_ALL)
    else:
        print(Fore.RED, 'Status code:' + str(+response.status_code))
        print(Style.RESET_ALL)


def del_post(w):
    delQ=input('Do You want to delete single or multiple posts? Select s or m ')
    if delQ=='s':
        a=input("Give post id to delete:")
        requests.delete(w+'/posts/'+a)
    elif delQ=='m':
        a,b=input('Select range of posts to delete').split()
        for p in range(int(a),int(b)+1):
            requests.delete(w + '/posts/'+str(p))
    else:
        print('Wrong answer, please select s or m')
        del_post(w)


def addUser(web,usrD):
    # assign POST request to constant
    UProfile = requests.post(web + '/profile', data=usrD)
    # print POST request in text extension
    print(UProfile.text)

