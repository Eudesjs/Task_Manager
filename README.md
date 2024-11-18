# Task_Manager
Projeto construir uma pequena Aplicação Web utilizando um Web Service ou um Banco de Dados.

# Projeto de Gerenciamento de Tarefas com Flask e SQLite

## Objetivo do Projeto

Este projeto consiste no desenvolvimento de uma aplicação web de **Gerenciamento de Tarefas** utilizando o framework **Flask** (Python) para o backend e o banco de dados **SQLite** para armazenamento dos dados. A aplicação oferece uma interface simples para realizar operações básicas como:

- **Adicionar** uma nova tarefa.
- **Visualizar** a lista de tarefas.
- **Editar** uma tarefa existente.
- **Excluir** tarefas.

O projeto exemplifica o conceito de um sistema **CRUD** (Create, Read, Update, Delete).

---

## Estrutura do Projeto

A aplicação é organizada com a seguinte estrutura de diretórios e arquivos:

---

## Funcionalidades

### 1. **Página Inicial** (`index.html`)
Exibe todas as tarefas cadastradas em uma lista, com opções para **editar** ou **excluir**. Também há um botão para adicionar novas tarefas.

### 2. **Adicionar Tarefa** (`add_task.html`)
Formulário simples onde o usuário pode inserir o **título** e a **descrição** de uma tarefa. Após preencher e enviar, a tarefa é salva no banco de dados.

### 3. **Editar Tarefa** (`edit_task.html`)
Carrega o formulário preenchido com os dados da tarefa selecionada para edição. O usuário pode alterar o título e/ou a descrição e salvar as alterações no banco.

### 4. **Deletar Tarefa**
A exclusão de uma tarefa é feita diretamente na página inicial, ao clicar no botão "Deletar".

---

## Tecnologias Utilizadas

- **Flask**: Framework web em Python para gerenciamento de rotas, processamento de formulários e renderização de templates HTML.
- **SQLite**: Banco de dados relacional leve, utilizado para armazenar as tarefas.
- **HTML/CSS**: Linguagens de marcação e estilo para criar a interface da aplicação.

---

## Detalhes Técnicos

### Banco de Dados
- A aplicação utiliza o banco SQLite, que cria o arquivo `database.db` automaticamente na primeira execução.
- Estrutura da tabela `tasks`:
  - `id` (inteiro, chave primária, autoincrementada)
  - `title` (texto, obrigatório)
  - `description` (texto, opcional)
- A função `init_db()` em `app.py` é responsável por criar a tabela, caso ela ainda não exista.

### Rotas e Funcionalidades
- **`/`**: Página inicial. Lista todas as tarefas.
- **`/add`**: Formulário para adicionar novas tarefas.
- **`/edit/<id>`**: Formulário para editar uma tarefa existente.
- **`/delete/<id>`**: Exclui uma tarefa com base no seu `id`.

### Execução da Aplicação
1. Certifique-se de ter o Python instalado e o Flask configurado:
   ```bash
   pip install flask
### Execute O Arquivo Principal
    python app.py

### Acesse a Aplicação no Navegador pelo Endereço
    http://127.0.0.1:5000/
