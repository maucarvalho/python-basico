nomes = ['Maurício', 'Guilherme', 'João', 'Julia']

for nome in nomes:
    print(nome)

lista_de_numeros = range(1,6)

for item in lista_de_numeros:
    print(item)

for i in range(len(nomes)):
    print(nomes[i])

i = 0 

while i < 10:
    print('O numero é menor que 10:', i)
    i = i +1
print('Fim do while, i vale:', i)