import requests
import json

cidade = input('Escreva o nome da Cidade:')

requisicao = requests.get('api', + cidade + 'api key')

print(requisicao)