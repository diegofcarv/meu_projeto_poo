from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo

def test_livro_fica_indisponivel_apos_emprestimo():
    usuario = Usuario("Danilo", "U001")
    livro = Livro("Capitães de Areia", "Jorge Amado", "L001")

    emprestimo = Emprestimo(usuario, livro)

    assert livro.disponivel is False
    assert emprestimo.ativo is True

import pytest

def test_nao_emprestar_livro_indisponivel():
    usuario1 = Usuario("Danilo", "U001")
    usuario2 = Usuario("Vinicius", "U002")
    livro = Livro("Capitães de Areia", "Jorge Amado", "L001")

    emprestimo1 = Emprestimo(usuario1, livro)

    with pytest.raises(ValueError):
        Emprestimo(usuario2, livro)