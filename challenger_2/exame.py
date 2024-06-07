from exame_handler import AprovaExameRaioX, AprovaExameSangue

class Exame:
    def __init__(self, tipo) -> None:
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador_sangue = AprovaExameSangue()
aprovador_raiox = AprovaExameRaioX()

aprovador_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovador_raiox.aprovar_solicitacao_exame(exame_raio_x)