# Desenvolva sua classe Copo aqui.
from .recipiente import Recipiente


class Copo(Recipiente):
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True, bebida: str = "água") -> None:
        self.bebida = bebida
        super().__init__(tamanho, conteudo=conteudo, limpo=limpo)

    def __repr__(self) -> str:
        message = f"Um copo de %.1fml contendo %.1fml de {self.bebida}" % (
            self.tamanho, self.conteudo)
        if self.conteudo == 0:
            message = f"Um copo vazio de %.1fml" % (self.tamanho)
        return message

    def __str__(self) -> str:
        message = f"Um copo de %.1fml contendo %.1fml de {self.bebida}" % (
            self.tamanho, self.conteudo)
        if self.conteudo == 0:
            message = f"Um copo vazio de %.1fml" % (self.tamanho)
        return message

    def encher(self, bebida: str = "água"):
        if self.esta_limpo():
            self.sujar()
            self.conteudo = self.tamanho
            self.bebida = bebida
        else:
            return "Não se pode encher um copo sujo"

    def beber(self, quantidade: float):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        self.conteudo = self.conteudo - quantidade

    def lavar(self):
        pass
        self.bebida = None
        self.conteudo = 0
        self.limpo = True
