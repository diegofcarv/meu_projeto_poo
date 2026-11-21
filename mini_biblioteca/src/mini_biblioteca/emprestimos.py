from .livros import Livro
from .usuarios import Usuario

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.livro = livro
        self.usuario = usuario

        if not livro.disponivel:
            raise ValueError("Livro indisponível para empréstimo")

        self.ativo: bool = True
        self.livro.disponivel: bool = False