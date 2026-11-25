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

def test_criacao_emprestimo():
    usuario = Usuario("Danilo", "U001")
    livro = Livro("Capitães de Areia", "Jorge Amado", "L001")

    emprestimo = Emprestimo(usuario, livro)

    assert emprestimo.usuario is usuario
    assert emprestimo.livro is livro
    assert emprestimo.ativo is True
    assert livro.disponivel is False

