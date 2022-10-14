headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}





import requests
import json
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from bs4 import BeautifulSoup

def login():
    url = 'http://prof.mo.mosreg.ru/api/login'
    s = requests.Session()
    payload = {
        'username': "username",
        'password': "password",
    }
    res = s.post('http://prof.mo.mosreg.ru/api/login', json=payload,headers=headers)

    s.headers.update(json.loads(res.content))

    x4 = str(s.headers['token'])
    headers2 = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Content-Type': 'application/json; charset=UTF-8',
    'Connection': 'Keep-Alive',
    'Cookie': f'auth-token=Token%20{x4}',
    }
    # url = "http://prof.mo.mosreg.ru/api/spoPetition/search/advancedSearch?page=1&size=500&sort=createdTs%2Cdesc&order=desc&q=%7B%22spoEducationYear%22%3A%224%22%2C%22status%22%3A%22ACCEPTED%22%7D&projection=grid"
 
    response = s.get(url,headers=headers2) 
    soup = BeautifulSoup(response.text, 'lxml')

    print(type(soup))
    with open("games_list.txt", "a", encoding='utf-8') as file:
        file.write(soup.text + '\n')
login()

