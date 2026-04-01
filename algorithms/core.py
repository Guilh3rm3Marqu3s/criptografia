from abc import abstractmethod, ABC

class Algorithm(ABC):
   
    @property
    @abstractmethod
    def nome(self) -> str:
        #Retorna o nome do algoritmo
        pass
    
    @property
    @abstractmethod
    def desc(self) -> str:
        # Retorna a descrição do algoritmo
        pass
        
    @abstractmethod
    def __call__(self, texto_entrada, **kwargs):
        # Classe que herdará deverá implementar obrigatoriamete esse método
        pass
    
        