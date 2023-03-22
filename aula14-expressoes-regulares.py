import re 

string_de_teste = 'O gata e gata é bonito'

padrao = re.search(r'gat.', string_de_teste)

if padrao:
    print(padrao.group())
else: 
    print('Padrão não encontrado')
