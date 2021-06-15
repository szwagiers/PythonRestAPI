import requests
web='http://localhost:3000'

de= requests.delete(web+'/posts/2')
de2= requests.delete(web+'/posts/3')
