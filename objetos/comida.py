from time import sleep


class Comida:
    
    # Atributos
    _peso_gramas: float
    _nome_comida: str
    __comida_pronta: bool
    
    
    # Getters
    @property
    def get_peso_gramas(self):
        return self._peso_gramas
    
    @property
    def get_nome_comida(self):
        return self._nome_comida
    
    @property
    def get_comida_pronta(self):
        return self.__comida_pronta


    # Métodos
    def preparar_comida(self, tempo_preparo):
        print(f"Preparando comida...")
        sleep(tempo_preparo)
        self.__comida_pronta = True
        
        