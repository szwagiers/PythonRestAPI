import requests
import json
import sqlite3
from colorama import Fore, Back, Style

#create database for user
userDB = sqlite3.connect('Users.db')

#set cursor
cur = userDB.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)''')


#assign webpage (JSON server) to constant
web='http://localhost:3000'

#assign GET request to constant
response = requests.get('http://localhost:3000')

#print response with status code
print(Fore.GREEN , 'Status code:'+str(+response.status_code))
print(Style.RESET_ALL)

#creating example value to upload
values ={'name': 'bob'}
#assign POST request to constant
post = requests.post(web+'/posts', data= values)
#print POST request in text extension
print(post.text)


#create new constant(dictionary) with new data to update existing file
change={'name':'John'}

#assign PUT request to constant with extended webpage address
put = requests.put(web+'/posts/3',data=change)

#print PUT request
print(put.text)

#assign GET request to new constant with updated data from webpage
change_req = requests.get(web+'/posts/3')

#print changes to earlier given post
print(change_req.text)