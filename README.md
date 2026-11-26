# Mini Biblioteca

Projeto desenvolvido para praticar Programação Orientada a Objetos (POO) e modularização utilizando Python.

O sistema representa o funcionamento básico de uma biblioteca, permitindo criar livros e usuários, realizar empréstimos e registrar devoluções.

## Funcionalidades

- Cadastro de livros por meio de objetos.
- Criação de usuários.
- Realização de empréstimos.
- Verificação da disponibilidade dos livros.
- Bloqueio de empréstimos de livros indisponíveis.
- Devolução de livros.

## Tecnologias

- Python 3
- uv
- pytest

## Estrutura do projeto

```text
meu_projeto_poo/
├── mini_biblioteca/
│   ├── src/
│   │   └── mini_biblioteca/
│   │       ├── __init__.py
│   │       ├── livros.py
│   │       ├── usuarios.py
│   │       ├── emprestimos.py
│   │       └── main.py
│   ├── tests/
│   │   ├── test_instanciacao.py
│   │   └── test_regras.py
│   ├── pyproject.toml
│   └── uv.lock
├── .gitignore
└── README.md
```

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/diegofcarv/meu_projeto_poo.git
```

### 2. Acessar a pasta do projeto

```bash
cd meu_projeto_poo/mini_biblioteca
```

### 3. Instalar as dependências

```bash
uv sync
```

### 4. Executar o programa

```bash
uv run python -m mini_biblioteca.main
```

## Testes

Para executar os testes automatizados, utilize:

```bash
uv run pytest .
```

Os testes verificam a criação dos objetos e o funcionamento das regras de empréstimo e devolução.
