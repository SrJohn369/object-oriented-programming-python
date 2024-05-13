from abc import ABC, abstractmethod



# classe atributos
class SerVivo:
    
    _nome: str
    _idade: int
    _sexo: str
    
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def sexo(self):
        return self._sexo
    
    
# Interface e Agregação
class SerVivoInterface(ABC):
    @abstractmethod
    def fazerSom(self):
        pass
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def beberAgua(self):
        pass
    
    @abstractmethod
    def fazerNecessidade(self):
        pass