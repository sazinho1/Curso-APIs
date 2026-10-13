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
Disciplinas: list[Disciplina] = [
    Disciplina(id=1, nome="PAA", professor="Henrique Viana", semestre="5", feita=False),
]
proximo_id = 2


def buscar_disciplina(disciplina_id: int) -> Disciplina:
    """Procura um disciplina pelo id. Se não achar, devolve erro 404."""
    for disciplina in Disciplinas:
        if disciplina.id == disciplina_id:
            return disciplina
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"disciplina com id {disciplina_id} não encontrado",
    )


# ---------------------------------------------------------------------------
# Rotas
# ---------------------------------------------------------------------------
@app.get("/")
def raiz():
    """Rota de boas-vindas, útil para testar se a API está no ar."""
    return {"mensagem": "API de disciplinas funcionando! Acesse /docs para testar."}


# READ (listar todos, com filtros opcionais)
@app.get("/disciplinas", response_model=list[Disciplinas])



# READ (buscar um por id)
@app.get("/disciplinas/{disciplina_id}", response_model=Disciplina)



# CREATE
@app.post("/disciplinas", response_model=Disciplina, status_code=status.HTTP_201_CREATED)



# UPDATE
@app.put("/disciplinas/{disciplina_id}", response_model=Disciplina)



# DELETE
@app.delete("/disciplinas/{disciplina_id}", status_code=status.HTTP_204_NO_CONTENT)

