"""
API de Livros - exemplo didático de CRUD com FastAPI.

Os dados ficam guardados em uma lista na memória (sem banco de dados).
Ao reiniciar o servidor, tudo volta ao estado inicial.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="API de Livros",
    description="Exemplo simples de CRUD para o curso de Introdução a APIs.",
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Modelos (definem o formato dos dados que entram e saem da API)
# ---------------------------------------------------------------------------
class LivroCriar(BaseModel):
    """Dados que o cliente envia para criar ou atualizar um livro."""

    titulo: str = Field(..., min_length=1, examples=["Dom Casmurro"])
    autor: str = Field(..., min_length=1, examples=["Machado de Assis"])
    ano: Optional[int] = Field(default=None, ge=0, le=2100, examples=[1899])
    lido: bool = False


class Livro(LivroCriar):
    """Livro completo, como a API devolve (inclui o id)."""

    id: int


# ---------------------------------------------------------------------------
# "Banco de dados" em memória
# ---------------------------------------------------------------------------
livros: list[Livro] = [
    Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis", ano=1899, lido=True),
    Livro(id=2, titulo="O Cortiço", autor="Aluísio Azevedo", ano=1890, lido=False),
    Livro(id=3, titulo="Capitães da Areia", autor="Jorge Amado", ano=1937, lido=False),
]
proximo_id = 4


def buscar_livro(livro_id: int) -> Livro:
    """Procura um livro pelo id. Se não achar, devolve erro 404."""
    for livro in livros:
        if livro.id == livro_id:
            return livro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Livro com id {livro_id} não encontrado",
    )


# ---------------------------------------------------------------------------
# Rotas
# ---------------------------------------------------------------------------
@app.get("/")
def raiz():
    """Rota de boas-vindas, útil para testar se a API está no ar."""
    return {"mensagem": "API de Livros funcionando! Acesse /docs para testar."}


# READ (listar todos, com filtros opcionais)
@app.get("/livros", response_model=list[Livro])
def listar_livros(autor: Optional[str] = None, lido: Optional[bool] = None):
    """Lista os livros. Filtros opcionais: ?autor=Machado&lido=true"""
    resultado = livros
    if autor is not None:
        resultado = [l for l in resultado if autor.lower() in l.autor.lower()]
    if lido is not None:
        resultado = [l for l in resultado if l.lido == lido]
    return resultado


# READ (buscar um por id)
@app.get("/livros/{livro_id}", response_model=Livro)
def obter_livro(livro_id: int):
    """Devolve um único livro pelo id."""
    return buscar_livro(livro_id)


# CREATE
@app.post("/livros", response_model=Livro, status_code=status.HTTP_201_CREATED)
def criar_livro(dados: LivroCriar):
    """Cadastra um novo livro. O id é gerado automaticamente."""
    global proximo_id
    novo = Livro(id=proximo_id, **dados.model_dump())
    livros.append(novo)
    proximo_id += 1
    return novo


# UPDATE
@app.put("/livros/{livro_id}", response_model=Livro)
def atualizar_livro(livro_id: int, dados: LivroCriar):
    """Substitui os dados de um livro existente."""
    livro = buscar_livro(livro_id)
    livro.titulo = dados.titulo
    livro.autor = dados.autor
    livro.ano = dados.ano
    livro.lido = dados.lido
    return livro


# DELETE
@app.delete("/livros/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_livro(livro_id: int):
    """Remove um livro. Não devolve conteúdo (204)."""
    livro = buscar_livro(livro_id)
    livros.remove(livro)
