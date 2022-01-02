from logging import exception
import requests as req

# try:
#     res = req.get('https://putsreq.com/H9PpxjWVQXrBWYlyDvSX')
#     print(res.text)
# except Exception as err:
#     print('Error:', err)

url = 'http://localhost:3030'

# try:
#     res = req.get(url)
#     res_js = res.json()
#     print(res_js)
#     for fruit in res_js['data']:
#         print(fruit)
# except Exception as err:
#     print('Error', err)

try:
    fruit = {'name': 'nova fruta 1'}
    res = req.post(url+'/new', data=fruit)
    print(res)
except Exception as err:
    print('Error:', err)