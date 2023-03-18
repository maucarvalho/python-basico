from contextlib import nullcontext


quantidade = input('Escreva a quantidade de convidados:')
i = 0
lista_nomes = []

while i < int(quantidade):
    nomes = input('Digite o nome do convidado:')
    i = i + 1
    lista_nomes.append(nomes)
print(lista_nomes)