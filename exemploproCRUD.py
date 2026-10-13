from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="API de Disciplinas do Curso de Computação",
    description="Exemplo simples de um exercício sobre fazer um CRUD para o curso de Introdução a APIs.",
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Modelos (definem o formato dos dados que entram e saem da API)
# ---------------------------------------------------------------------------
class DisciplinaCriar(BaseModel):
    """Dados que o cliente envia para criar ou atualizar um disciplina."""

    nome: str = Field(..., min_length=1, examples=["Programação Orientada a Objeto"])
    professor: str = Field(..., min_length=1, examples=["Paulo Henrique"])
    semestre: Optional[int] = Field(default=None, ge=1, le=10, examples=[2])
    feita: bool = False


class Disciplina(DisciplinaCriar):
    """Disciplina completa, como a API devolve (inclui o id)."""

    id: int


# ---------------------------------------------------------------------------
# "Banco de dados" em memória
# ---------------------------------------------------------------------------
disciplinas: list[Disciplina] = [
    Disciplina(id=1, nome="PAA", professor="Henrique Viana", semestre=5, feita=False),
]
proximo_id = 2


def buscar_disciplina(disciplina_id: int) -> Disciplina:
    """Procura um disciplina pelo id."""
    for disciplina in disciplinas:
        if disciplina.id == disciplina_id:
            return disciplina
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Disciplina com id {disciplina_id} não encontrada",
    )
        
# ---------------------------------------------------------------------------
# Rotas
# ---------------------------------------------------------------------------
@app.get("/")
def raiz():
    """Rota de boas-vindas, útil para testar se a API está no ar."""
    return {"mensagem": "API de disciplinas funcionando! Acesse /docs para testar."}


# ============================ NÍVEL 1 ======================================
# READ (listar todas)
@app.get("/disciplinas", response_model=list[Disciplina])
def listar_disciplinas():
    # TODO: devolver a lista de disciplinas
    pass
 
 
# READ (buscar uma por id)
@app.get("/disciplinas/{disciplina_id}", response_model=Disciplina)
def obter_disciplina(disciplina_id: int):
    # TODO: devolver a disciplina com esse id
    # Dica: já existe uma função pronta que busca e trata o erro 404
    pass
 
 
# ============================ NÍVEL 2 ======================================
# CREATE
@app.post(
    "/disciplinas", response_model=Disciplina, status_code=status.HTTP_201_CREATED
)
def criar_disciplina(dados: DisciplinaCriar):
    # TODO:
    # 1. Declarar "global proximo_id"
    # 2. Criar uma Disciplina com id=proximo_id e os campos de "dados"
    #    Dica: Disciplina(id=proximo_id, **dados.model_dump())
    # 3. Adicionar a nova disciplina na lista
    # 4. Somar 1 em proximo_id
    # 5. Devolver a nova disciplina
    pass
 
 
# DELETE
@app.delete("/disciplinas/{disciplina_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_disciplina(disciplina_id: int):
    # TODO:
    # 1. Buscar a disciplina (com a função pronta)
    # 2. Removê-la da lista
    pass
 
 
# ============================ NÍVEL 3 (BÔNUS) ==============================
# UPDATE
@app.put("/disciplinas/{disciplina_id}", response_model=Disciplina)
def atualizar_disciplina(disciplina_id: int, dados: DisciplinaCriar):
    # TODO:
    # 1. Buscar a disciplina
    # 2. Atualizar nome, professor, semestre e feita com os valores de "dados"
    # 3. Devolver a disciplina atualizada
    pass
 