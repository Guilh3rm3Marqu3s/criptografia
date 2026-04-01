from abc import abstractmethod, ABC

class Algorithm(ABC):
   
    def __init_subclass__(cls, **kwargs):
       super().__init_subclass__(**kwargs)
       for attr in ['NOME', 'DESC']:
            if not hasattr(cls, attr):
                raise TypeError(f"A classe {cls.__name__} não definiu o atributo estático '{attr}'")
        
    @abstractmethod
    def __call__(self, texto_entrada, **kwargs):
        # Classe que herdará deverá implementar obrigatoriamete esse método
        pass
    
        