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

print("ESTADO INICIAL DO LIVRO")
print(
    f"Título: {livro1.titulo}\n", 
    f"Autor: {livro1.autor}\n", 
    f"Código do livro: {livro1.codigo}\n",
    f"Disponível: {livro1.disponivel}"
)

print("APÓS REALIZAR O EMPRÉSTIMO")
emprestimo1 = Emprestimo(usuario1, livro1)

print(f"Usuário que recebeu: {usuario1.nome}")
print(f"Livro emprestado: {livro1.titulo}")
print(f"Livro disponível: {livro1.disponivel}")
print(f"Empréstimo ativo: {emprestimo1.ativo}")

print("APÓS REALIZAR A DEVOLUÇÃO")
emprestimo1.devolver()

print(f"Usuário que devolveu: {usuario1.nome}")
print(f"Livro devolvido: {livro1.titulo}")
print(f"Livro disponível: {livro1.disponivel}")
print(f"Empréstimo ativo: {emprestimo1.ativo}")