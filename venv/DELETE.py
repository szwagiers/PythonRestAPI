import requests
web='http://localhost:3000'


def del_post():
    a=input("Give post id to delete:")
    requests.delete(web+'/posts/'+a)

del_post()