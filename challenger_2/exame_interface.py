from abc import ABC, abstractmethod

class ExameInterface(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass
    
    @abstractmethod
    def verifica_condicoes_exame(self, exame):
        pass

    