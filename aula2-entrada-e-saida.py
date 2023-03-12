from multiprocessing.connection import wait
from unittest import result


print('Hello World! \nHello!')
print('Bye World!')

######################################################################################################

nome = 'Maurício'
sobrenome = input('Escreva seu Sobrenome: ')
idade = 30
tipo_nome = type(nome)
tipo_idade = type(idade)

print(nome, sobrenome, 'tem', idade, 'anos.')
print(nome + ' tem ' + str(idade) + ' anos.')

frase = nome + ' tem ' + str(idade) + ' anos.'
print(frase)

######################################################################################################

n1 = 2
n2 = 3
op = input('Qual operação vc deseja? ')

resultado = (int(n1), int(op), int(n2)) 

print(resultado)