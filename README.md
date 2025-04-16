# Intro
Este repositório contém material de apoio para a disciplina de Programação com Acesso a Banco de Dados ministrada pelo professor Gilbran Andrade.

## Sumário
1. [Ambiente Virtual Python](#-ambiente-virtual-python)
2. [Introdução Flask](#-código-base-em-flask)

---

## Ambiente Virtual Python
Ferramenta que permite criar um ambiente isolado para projetos em Python. Isso significa que você pode instalar bibliotecas e dependências específicas para um projeto sem afetar o restante do sistema ou outros projetos.

### 1. Criar um Ambiente Virtual

```bash
python -m venv nome_do_ambiente
```

Cria um novo ambiente virtual com o nome especificado (`nome_do_ambiente`). Ele será utilizado para isolar as dependências do projeto, evitando conflitos com outros projetos Python no seu sistema.

**Exemplo**:
```bash
python -m venv .venv
```

No exemplo acima, o ambiente virtual foi criado com o nome `.venv`

---

### 2. Ativar o Ambiente Virtual (Windows)

```bash
nome_do_ambiente\Scripts\activate.bat
```

Ativa o ambiente virtual em sistemas Windows, permitindo que os pacotes instalados fiquem restritos ao projeto atual.

**Exemplo**:
```bash
.venv\Scripts\activate.bat
```

> Após a ativação, você verá o nome do ambiente virtual no início da linha de comando.

---

### 3. Gerar o arquivo `requirements.txt`

```bash
pip freeze > requirements.txt
```

Gera um arquivo `requirements.txt` com todas as bibliotecas instaladas no ambiente virtual e sua versão. Esse arquivo é útil para compartilhar as dependências com outros desenvolvedores ou na utilização de diferentes computadores.

> É uma boa prática executar este comando sempre que terminar de trabalhar no ambiente virtual.

---

### 4. Instalar bibliotecas a partir do `requirements.txt`

```bash
pip install -r requirements.txt
```

Instala automaticamente todas as bibliotecas listadas no arquivo `requirements.txt`, garantindo que o ambiente de desenvolvimento esteja configurado corretamente.

> É uma boa prática executar este comando sempre que criar e ativar um novo ambiente virtual.

---

## Introdução Flask

Para instalar o módulo do **Flask** no seu ambiente virtual utilize `pip install flask`

Para iniciar a execução da aplicação Flask utilize:

```bash
flask run
```

Abaixo está um exemplo do código base de uma aplicação web desenvolvida com o **Flask**, um microframework Python para desenvolvimento de aplicações web.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
     return "Olá Mundo"
```

### Explicação

- `from flask import Flask`  
  Importa a classe `Flask` do framework. Essa classe será usada para criar a aplicação.

- `app = Flask(__name__)`  
  Cria uma instância da aplicação Flask. O parâmetro `__name__` indica o nome do módulo atual e é necessário para que o Flask encontre os recursos da aplicação.

```python
@app.route("/")
def inicio():
    return "Olá Mundo"
```

Define a rota principal (URL raiz `/`). Quando o usuário acessa essa rota no navegador, o Flask retorna o texto **"Olá Mundo"**.

**Exemplo de uso:**

Acessando `http://localhost:5000/`, o navegador exibirá: `Olá Mundo`

---

### Utilizando Rota Dinâmica no Flask

No Flask, uma rota define o endereço (URL) que um usuário pode acessar no navegador para interagir com sua aplicação. Enquanto rotas estáticas retornam sempre o mesmo conteúdo (ex: /), as rotas dinâmicas permitem capturar partes da URL como variáveis.

As rotas dinâmicas são caracterizadas pelo nome do parâmetro ser definido os símbolos de maior que e menor que, exemplo: `<variavel>`.

```python
@app.route("/<palavra>")
def magica(palavra):
    return palavra
```

Nesta rota dinâmica o que for escrito após a `/` será capturado como argumento da função `magica()` e retornado como resposta.

**Exemplo de uso:**

Acessando `http://localhost:5000/ifrn`, o navegador exibirá: `ifrn`

Acessando `http://localhost:5000/tapioca`, o navegador exibirá: `tapioca`


