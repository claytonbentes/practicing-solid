from exame_interface import ExameInterface

class AprovaExameSangue(ExameInterface):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Exame sanguíneo aprovado!")
    
    def verifica_condicoes_exame(self, exame):
        return exame.tipo == "sangue"

class AprovaExameRaioX(ExameInterface):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("RaioX aprovado")

    def verifica_condicoes_exame(self, exame):
        return exame.tipo == "raio-x"