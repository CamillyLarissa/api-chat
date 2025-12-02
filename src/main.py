from fastapi import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
    message: str
    

app = FastAPI()

# . Endpoint de Chat: Crie um endpoint POST /chat que aceite uma 
# mensagem de texto do usuário e retorne a resposta do Agente de IA. 
# ● O payload de entrada deve ser um JSON simples com o campo 
# message. 
# ● A resposta deve ser um JSON com o campo response. 

@app.post("/chat")

def get_user(message: Message):
    # Simulando uma resposta do agente de IA
    response = f"Você disse: {message.message}. Esta é a resposta do agente de IA."
    return {"response": response}