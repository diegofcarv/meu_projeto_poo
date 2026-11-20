class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.livro = livro
        self.usuario = usuario
        self.ativo: bool = True