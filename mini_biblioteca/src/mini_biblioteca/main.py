from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo

usuario1 = Usuario(
    nome = "Danilo",
    id_usuario = "U001"
)
livro1 = Livro(
    titulo = "Capitães de Areia",
    autor = "Jorge Amado", 
    codigo = "L001"
)

emprestimo1 = Emprestimo(usuario1, livro1)
emprestimo1.devolver()