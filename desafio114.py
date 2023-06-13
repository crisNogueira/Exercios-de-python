import requests

url = 'http://www.pudim.com.br/'

try:
    if requests.get(url).status_code == 200:
        print('\033[32mO site está disponivel\033[m')
except:
    print('\033[31mO site não está disponivel\033[m')
