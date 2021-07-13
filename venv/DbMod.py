import sqlite3
from encryption import *
from colorama import Fore, Back, Style

#create database for user/connect to databese
userDB = sqlite3.connect('Users.db')

#set cursor
cur = userDB.cursor()

#create table for users data
cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,login TEXT UNIQUE ,password TEXT)''')
userDB.commit()


#cur.execute(("SELECT * FROM {}").format(Tname))
#userDB.commit()
#cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

#print(cur.fetchall())


def insData(log,pswrd):
    cur.execute('''INSERT INTO users(login,password) VALUES ('{}','{}')'''.format(log,pswrd))
    userDB.commit()


def selUsrData():
    cur.execute('''SELECT * FROM users ''')
    table = cur.fetchall()
    # print(table)
    for row in table:
        # print(row)
        print('id=', row[0],'login=', row[1],'password=', row[2])
        # print('login=', row[1])
        # print('password=', row[2])


def checkLogIn(log,pswrd):
    cur.execute('''SELECT *  FROM users''')
    userDB.commit()
    check=cur.fetchall()
    if check:
        # if log==dbLog and pswrd==dePsw:
        print(Fore.GREEN,'Logged in successfully')
        print(Style.RESET_ALL)

# cur.execute('''SELECT * FROM users''')
# print(userDB.fetchall())

