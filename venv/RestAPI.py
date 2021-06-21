# import requests
# import json
# import sqlite3
from colorama import Fore, Back, Style
from DbMod import *
from Req_Mod import *
from UserMenuMod import *

#assign webpage (JSON server) to constant
web='http://localhost:3000'

ConCheck(web)

#create database for user
userDB = sqlite3.connect('Users.db')
#set cursor
cur = userDB.cursor()

usrMenu()

selUsrData()


#create new constant(dictionary) with new data to update existing file
#change={'name':'John'}

#assign PUT request to constant with extended webpage address
#put = requests.put(web+'/posts/3',data=change)

#print PUT request
# print(put.text)
#
# #assign GET request to new constant with updated data from webpage
# change_req = requests.get(web+'/posts/3')
#
# #print changes to earlier given post
# print(change_req.text)