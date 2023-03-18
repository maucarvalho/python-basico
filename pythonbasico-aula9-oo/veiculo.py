class Veiculo:
    
    def __init__(self, cor, marcas, rodas, tanque):
        self.cor = cor
        self.marcas = marcas
        self.rodas = rodas
        self.tanque = tanque
    
    def abastecer(self, litros):
        self.tanque += litros
        
