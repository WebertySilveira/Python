import requests
import json

process = input()
process = process.replace('.', '')
process = process.replace('-', '')

url = "https://python.doc9.com.br/api/teste_programador/?processo=" + process
header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
request = requests.get(url, headers = header).json()