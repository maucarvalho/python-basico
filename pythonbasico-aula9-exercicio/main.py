from http import client
from traceback import print_tb
from cliente import Cliente
from conta import Conta

people1 = Cliente('Maurício', '0202020202', '30')
conta_people1 = Conta(people1, 1000, 2000)

print('Nome:', people1.nome)
print('CPF:', people1.cpf)
print('Idade:', people1.idade)
print('Saldo:', conta_people1.saldo)
print('Limite:', conta_people1.limite)

conta_people1.deposito(300)
print('Novo Saldo:', conta_people1.saldo)

conta_people1.saque(500)
print('Novo Saldo:', conta_people1.saldo)

conta_people1.consulta()
print('Novo Saldo:', conta_people1.saldo)