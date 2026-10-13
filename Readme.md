# 📚 API de Livros com FastAPI

Exemplo simples de API REST com **CRUD completo** (criar, ler, atualizar e remover livros), feito para o curso de **Introdução a APIs**.

Os dados ficam guardados **na memória** (uma lista Python), então não é preciso instalar banco de dados. Ao reiniciar o servidor, os dados voltam ao estado inicial.

## O que você vai aprender

- Rodar uma API localmente
- Testar uma API pelo navegador (Swagger), pelo Postman e pelo VS Code
- Entender como os métodos HTTP se relacionam com o CRUD

| Operação CRUD | Método HTTP | Rota            | O que faz                 |
|---------------|-------------|-----------------|---------------------------|
| Read (lista)  | GET         | `/livros`       | Lista todos os livros     |
| Read (um)     | GET         | `/livros/{id}`  | Busca um livro pelo id    |
| Create        | POST        | `/livros`       | Cadastra um novo livro    |
| Update        | PUT         | `/livros/{id}`  | Atualiza um livro         |
| Delete        | DELETE      | `/livros/{id}`  | Remove um livro           |

---

## Pré-requisitos

- [Python 3.9 ou superior](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/) (ou outro editor)
- (Opcional) [Postman](https://www.postman.com/downloads/)

Para conferir se o Python está instalado, rode no terminal:

```bash
python --version
```

> Em alguns sistemas (Linux/Mac) o comando pode ser `python3`.

---

## Passo a passo para rodar

### 1. Baixe o projeto

Clone o repositório (ou baixe a pasta) e entre nela:

```bash
git clone <URL-DO-REPOSITORIO>
cd api-livros
```

### 2. Crie um ambiente virtual

O ambiente virtual isola as dependências deste projeto das do resto do computador.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Se deu certo, aparecerá `(venv)` no início da linha do terminal.

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie o servidor

```bash
fastapi dev main.py
```

Se o comando acima não funcionar, use a alternativa:

```bash
uvicorn main:app --reload
```

O terminal vai mostrar algo como:

```
Uvicorn running on http://127.0.0.1:8000
```

Pronto, a API está no ar! 🎉 O modo `dev` (ou `--reload`) reinicia o servidor automaticamente sempre que você salva o código.

### 5. Teste no navegador

Abra:

- **http://127.0.0.1:8000/** → mensagem de boas-vindas
- **http://127.0.0.1:8000/livros** → lista de livros em JSON
- **http://127.0.0.1:8000/docs** → **documentação interativa (Swagger)**, gerada automaticamente

---

## Como testar a API

### Opção A: Swagger (`/docs`), a mais fácil

1. Acesse http://127.0.0.1:8000/docs
2. Clique em uma rota (por exemplo, `POST /livros`)
3. Clique em **Try it out**
4. Edite o JSON de exemplo
5. Clique em **Execute** e veja a resposta (status code e corpo) logo abaixo

### Opção B: Postman

1. Crie uma nova requisição e escolha o método (GET, POST, etc.)
2. Use a URL `http://127.0.0.1:8000/livros`
3. Para POST e PUT: aba **Body** → **raw** → formato **JSON**, e cole:

```json
{
  "titulo": "Vidas Secas",
  "autor": "Graciliano Ramos",
  "ano": 1938,
  "lido": false
}
```

4. Clique em **Send**

### Opção C: dentro do VS Code

Instale a extensão **REST Client** e abra o arquivo `requests.http` deste projeto. Clique em **Send Request** acima de cada bloco. Alternativa: a extensão **Thunder Client**.

### Opção D: terminal (curl)

```bash
# Listar
curl http://127.0.0.1:8000/livros

# Criar
curl -X POST http://127.0.0.1:8000/livros \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "ano": 1938}'

# Apagar
curl -X DELETE http://127.0.0.1:8000/livros/1
```

---

## Status codes usados

| Código | Significado                                  | Onde aparece                         |
|--------|----------------------------------------------|--------------------------------------|
| 200    | OK                                           | GET e PUT com sucesso                |
| 201    | Criado                                       | POST com sucesso                     |
| 204    | Sem conteúdo                                 | DELETE com sucesso                   |
| 404    | Não encontrado                               | id inexistente                       |
| 422    | Dados inválidos                              | JSON fora do formato esperado        |

---

## Estrutura do projeto

```
api-livros/
├── main.py           # código da API
├── requirements.txt  # dependências
├── requests.http     # requisições de teste (extensão REST Client)
└── README.md         # este arquivo
```

## Problemas comuns

- **`fastapi: command not found`**: o ambiente virtual não está ativado, ou as dependências não foram instaladas. Refaça os passos 2 e 3.
- **`Address already in use`**: já existe algo rodando na porta 8000. Use outra porta: `fastapi dev main.py --port 8001`.
- **No Windows, o `activate` é bloqueado**: no PowerShell, rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e tente de novo.

## Links úteis

- Documentação oficial do FastAPI: https://fastapi.tiangolo.com
- Tutorial oficial (em português): https://fastapi.tiangolo.com/pt/tutorial/
