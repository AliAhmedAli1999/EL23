import requests as req
import time

while 1 :
    res = req.get('https://www.boredapi.com/api/activity')
    content = res.json()
    time.sleep(10)
    print(content['activity'])

