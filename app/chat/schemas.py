from pydantic import BaseModel, Field

class Response(BaseModel):
    response: str = Field(description="Resposta gerada pelo modelo de linguagem.",
                          examples=["A resposta é 12"])

class Message(BaseModel):
    message: str = Field(min_length=1, description="Mensagem enviada pelo usuário.",
                         examples=["Quanto é a raiz quadrada de 144?"])