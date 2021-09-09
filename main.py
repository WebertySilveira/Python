import requests

header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
request = requests.get("https://python.doc9.com.br/api/teste_programador/?processo=00003825420205170014", headers = header).json()