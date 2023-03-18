from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, cor, marcas, tanque):
        Veiculo.__init__(self, cor, marcas, 4, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Erro: O tanque já está cheio.")
        else:
            self.tanque += litros
