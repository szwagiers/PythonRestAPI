import requests
import json
import sqlite3
from colorama import Fore, Back, Style
from DbMod import insData,selData

#create database for user
userDB = sqlite3.connect('Users.db')

#set cursor
cur = userDB.cursor()

#assign webpage (JSON server) to constant
web='http://localhost:3000'

#assign GET request to constant
response = requests.get('http://localhost:3000')



#Insert data from user
n,s = input('Please provied your data: ').split()

def cr_user(n,s):
    user={'name':n,'surname':s}
    return user

u=cr_user(n,s)

#assign POST request to constant
post = requests.post(web+'/posts', data= u)

insData(n,s)

#print POST request in text extension
print(post.text)
selData()






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