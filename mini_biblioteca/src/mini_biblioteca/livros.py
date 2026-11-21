class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel: bool = True

livro1 = Livro("Dom Casmurro", "Machado de Assis", "L001")
livro2 = Livro("O Cortiço", "Aloísio Azevedo", "L002")