from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo

def test_criacao_livro():
    livro = Livro("Capitães de Areia", "Jorge Amado", "L001")

    assert livro.titulo == "Capitães de Areia"
    assert livro.autor == "Jorge Amado"
    assert livro.codigo == "L001"
    assert livro.disponivel is True

def test_criacao_usuario():
    usuario = Usuario("Danilo", "U001")

    assert usuario.nome == "Danilo"
    assert usuario.id_usuario == "U001"