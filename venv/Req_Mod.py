import requests
from colorama import Fore, Back, Style
web='http://localhost:3000'

#print response with status code
def ConCheck(w):
    response = requests.get(w)
    print(Fore.GREEN, 'Status code:' + str(+response.status_code))
    print(Style.RESET_ALL)

def del_post(w,a):
    #a=input("Give post id to delete:")
    requests.delete(web+'/posts/'+str(a))

for a in range(2,7):
    del_post(web,a)