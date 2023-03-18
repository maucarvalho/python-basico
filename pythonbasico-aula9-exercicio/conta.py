from cliente import Cliente

class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
    
    def deposito(self, deposito):
        self.saldo += deposito

    def saque (self, saque):
        self.saldo -=saque

    def consulta (self):
        self.saldo