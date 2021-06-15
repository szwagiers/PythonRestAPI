import requests
import json
import tkinter

web='http://localhost:3000'

response = requests.get('http://localhost:3000')

print(response.status_code)

# values ={'name': 'bob'}
#
# post = requests.post(web+'/posts', data= values)
#
# print(post.text)

change={'name':'John'}
put = requests.put(web+'/posts/3',data=change)
print(put.text)

change_req = requests.get(web+'/posts/3')
print(change_req.text)