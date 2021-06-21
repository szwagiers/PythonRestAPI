from DbMod import *
import requests
from colorama import Fore, Back, Style
web='http://localhost:3000'

#print response with status code
def ConCheck(w):
    response = requests.get(w)
    print(Fore.GREEN, 'Status code:' + str(+response.status_code))
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


def addUser(usrD):
    # assign POST request to constant
    prof = requests.post(web + '/profile', data=usrD)
    # print POST request in text extension
    print(prof.text)
