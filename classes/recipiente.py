# Desenvolva sua classe Recipiente aqui.

class Recipiente:

    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True) -> None:
        if tamanho < 0:
            tamanho = 0
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.limpo = limpo

    def __repr__(self) -> str:
        message = "vazio"
        if self.conteudo > 0:
            message = "cheio"
        return f"Um recipiente {self.estado()} não especificado"

    def __str__(self) -> str:
        message = "vazio"
        if self.conteudo > 0:
            message = "cheio"
        return f"Um recipiente {self.estado()} não especificado"

    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        return False

    def lavar(self):
        self.conteudo = 0
        self.limpo = True

    def esta_limpo(self):
        if self.limpo:
            return True
        return False

    def estado(self):
        if self.limpo:
            return "limpo"
        return "sujo"

    def sujar(self):
        self.limpo = False
