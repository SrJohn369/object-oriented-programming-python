from .servivo import SerVivo, SerVivoInterface


# Herança e Inmplementação
class Pessoa(SerVivo, SerVivoInterface):
    
    __altura: float
    
    def __init__(self, altura, nome, idade, sexo):
        super().__init__(nome=nome, idade=idade, sexo=sexo)
        self.__altura = altura
        
    
    def fazerSom(self):
        print(f"{self.nome} está fazendo um som")
        
    
    def comer(self):
        print(f"{self.nome} está comendo")