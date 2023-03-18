from veiculo import Veiculo
from carro import Carro

veiculo1 = Veiculo('Azul', 'Hyundai','4', 30)

# print(veiculo1)
# print(type(veiculo1))

print('Cor:', veiculo1.cor)
print('Marca:', veiculo1.marcas)
print('Rodas:', veiculo1.rodas)
print('Tanque:', veiculo1.tanque)
print('')

veiculo2 = Carro('Preto', 'Ford', 20)
print('Cor:', veiculo2.cor)
print('Marca:', veiculo2.marcas)
print('Rodas:', veiculo2.rodas)
print('Tanque:', veiculo2.tanque)
print('')

veiculo1.abastecer(5)
print('Marca:', veiculo1.tanque)