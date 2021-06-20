import sqlite3

#create database for user/connect to databes
userDB = sqlite3.connect('Users.db')

#set cursor
cur = userDB.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,login UNIQUE TEXT,password TEXT)''')
userDB.commit()

#cur.execute(("SELECT * FROM {}").format(Tname))
#userDB.commit()
#cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

#print(cur.fetchall())


def insData(log,pswrd):
    cur.execute('''INSERT INTO users(Login,Password) VALUES ('{}','{}')'''.format(log,pswrd))
    userDB.commit()


def selData():
    cur.execute('''SELECT * FROM users''')
    for row in cur:
        print('id=', row[0])
        print('name=', row[1])
        print('surname=', row[2])

#print(cur.fetchall())

# cur.execute('''SELECT * FROM users''')
# print(userDB.fetchall())