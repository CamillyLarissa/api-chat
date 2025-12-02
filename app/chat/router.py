from fastapi import APIRouter, HTTPException, Request
from chat.schemas import Message, Response
from chat.service import create_message 

router = APIRouter()

@router.post("/chat", 
             response_model=Response, 
             status_code=200,
             name="Chat Endpoint",
             tags=["Chat"], 
             description="Recebe uma mensagem do usuário e retorna a resposta gerada pelo agente de chat IA.",
             responses={
                 200: {
                     "description": "Resposta gerada com sucesso.",
                     "content": {
                         "application/json": {
                             "example": {"response": "A raiz quadrada de 144 é 12."}
                         }
                     }
                 },
                 422: {
                     "description": "Erro de Validação (Pydantic)",
                     "content": {
                         "application/json": {
                             "example": {
                                 "detail": [
                                     {
                                         "loc": ["body", "message"],
                                         "msg": "field required",
                                         "type": "value_error.missing"
                                     }
                                 ]
                             }
                         }
                     }
                 },
                 500: {
                     "description": "Erro Interno (Capturado pelo Global Handler).",
                     "content": {
                         "application/problem+json": {
                             "example": {
                                 "tipo_erro": "ConnectionError", 
                                 "mensagem": "Max retries exceeded with url: /api/generate",
                                 "nota": "Ocorreu um erro interno no servidor."
                             }
                         }
                     }
                 }
             }
)
async def chat_endpoint(message: Message):

    
    message_dict = message.model_dump()
    
    resposta_texto = create_message(message_dict["message"])

    return {"response": resposta_texto}

