from .livros import Livro
from .usuarios import Usuario

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.livro = livro
        self.usuario = usuario

        if not livro.disponivel:
            raise ValueError("Livro indisponível para empréstimo")

        self.ativo = True
        self.livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True