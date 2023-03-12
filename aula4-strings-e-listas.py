frase = 'Oi, tudo bem?'
frase_lista = ['Nicole', 'Manuela', 'Renata', 'Laura', 'Maurício']
frase_lista.append('Maurício')
frase_lista.remove('Manuela')
frase_lista.insert(1, 'Luis')
frase_lista[0] = 'Ricardo'
frase_lista.count

contador_mau = frase_lista.count('Maurício')

print(frase_lista)
print(len(frase_lista))
print(contador_mau)
print(frase)
print(frase.lower())


frase_separada = frase.split(', ')
print(frase_separada[0])

frase_nova = frase + ' Como vai você?'

print(frase_nova)