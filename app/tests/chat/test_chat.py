from http import HTTPStatus
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_endpoint_calculo():
    
    """
    Testa se o endpoint responde corretamente a uma pergunta matemática que exige o uso da Tool.
    """
    response = client.post("/api/chat", json={"message": "Quanto é a raiz quadrada de 144?"})  
    assert response.status_code == HTTPStatus.OK  

    data = response.json()

    assert "response" in data
    assert "12" in data["response"] 

def test_chat_endpoint_conversa():
    """
    Testa se o endpoint responde a uma conversa normal sem quebrar.
    """
    response = client.post("/api/chat", json={"message": "Olá, tudo bem?"})
    
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["response"]) > 0