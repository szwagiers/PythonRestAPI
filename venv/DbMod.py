import sqlite3
from encyption import *
from colorama import Fore, Back, Style

#create database for user/connect to databes
userDB = sqlite3.connect('Users.db')

#set cursor
cur = userDB.cursor()

#create table for users data
cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,login TEXT UNIQUE ,password TEXT)''')
userDB.commit()
#create table for storing password data
cur.execute('''CREATE TABLE IF NOT EXISTS pswrds (id INTEGER PRIMARY KEY,keyVal text,FOREIGN KEY (id) REFERENCES users(id))''')
userDB.commit()

#cur.execute(("SELECT * FROM {}").format(Tname))
#userDB.commit()
#cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

#print(cur.fetchall())


def insData(log,pswrd):
    k,p= encrypt(pswrd)
    cur.execute('''INSERT INTO users(login,password) VALUES ({},{})'''.format(log,p))
    userDB.commit()
    cur.execute('''INSERT INTO pswrds(keyVal) VALUES({})'''.format(str(k)))


def selUsrData():
    cur.execute('''SELECT * FROM users''')
    for row in cur:
        print('id=', row[0])
        print('login=', row[1])
        print('password=', row[2])


def checkLogIn(log,pswrd):
    cur.execute('''SELECT u.id,login,password,keyVal  FROM users as u JOIN pswrds as p on u.id=p.id ''')
    userDB.commit()
    check=cur.fetchall()
    c_suite = Fernet(check[3])
    dePsw=c_suite.decrypt(check[2])
    dbLog=check[1]
    if log==dbLog and pswrd==dePsw:
        print(Fore.GREEN,'Logged succesfully')

# cur.execute('''SELECT * FROM users''')
# print(userDB.fetchall())