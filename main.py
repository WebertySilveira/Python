import requests
import json

process = input()
clearProcess = process.replace('.', '')
clearProcess = clearProcess.replace('-', '')

url = "https://python.doc9.com.br/api/teste_programador/?processo=" + clearProcess
header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
request = requests.get(url, headers = header).json()


ativo = {}
for i in request['poloAtivo']:
  ativo.update([('nome', i['nome']), ('tipo', i['tipo'])])

passivo = {}
for j in request['poloPassivo']:
  passivo.update([('nome', j['nome']), ('tipo', j['tipo'])])

itens = {}
for k in request['itensProcesso']:
  itens.update([('titulo', k['titulo']), ('data', k['data'])])

list = {
    'numero_processo' : process,
    'numero_processo_limpo' : clearProcess,
    'orgao' : request['orgaoJulgador'],
    'polo_ativo' : [
        {
            'nome' : ativo['nome'], 
            'tipo' : ativo['tipo'],
        }
    ],
    'polo_Passivo' : [
        {
            'nome' : passivo['nome'], 
            'tipo' : passivo['tipo'],
        }
    ],
    'movimentacoes' : [
        {
            'titulo' : itens['titulo'],
            'data' : itens['data'],
        }
    ],
}

print(json.dumps(list, indent=4))