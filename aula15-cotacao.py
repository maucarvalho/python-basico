from urllib import request
import requests
import json

requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')

cotacao = json.loads(requisicao.text)

print(cotacao['valores'])