import requests
import json


url = "https://www.naver.com/"
resp = requests.get(url)

# print(resp)

data = resp.json()


print(data)