import requests

cabecalho = {'User-agente':'iOS'}

texto = None
try: 
    requisicao = requests.get('https://google.com')
    texto = requisicao.text
except Exception as e:
    print('Requisicao deu erro: ', e)

print(texto)