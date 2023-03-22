import requests
import json

req = None

try:
    req = requests.get('http://www.omdbapi.com/?t=interstellar')
except:
    print('Erro na Conexão')
    exit()

dicionario = json.loads(req.text)


print('Titulo: ', dicionario['Title'])