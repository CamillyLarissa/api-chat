
Este projeto implementa uma API RESTful utilizando FastAP* integrada a um Agente de IA (Strands SDK** + **Ollama) capaz de realizar conversas naturais e executar cálculos matemáticos precisos através de ferramentas personalizadas (Tools).

## Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI:** Framework web moderno e de alta performance.
* **Strands Agents:** SDK para orquestração do Agente de IA.
* **Ollama:** LLM executado localmente (Modelo utilizado: Llama 3 ou similar).
* **Pytest:** Testes automatizados de integração.

## Pré-requisitos

1.  **Python 3.10** ou superior instalado.
2.  **Ollama** instalado e rodando.
    * Baixe em: https://ollama.com/
    * Baixe o modelo (exemplo com llama3.2):
        ```bash
        ollama pull llama3.2
        ```

## Instalação

1.  Clone o repositório e entre na pasta:
    ```bash
    git clone https://github.com/CamillyLarissa/api-chat.git
    cd app
    ```

2.  Crie e ative um ambiente virtual:
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Linux/Mac
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração (.env)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
STRANDS_OLLAMA_HOST=http://localhost:11434
STRANDS_OLLAMA_MODEL=llama3

## Instalação

uvicorn app.main:app --reload

A documentação interativa (Swagger UI) estará disponível em: http://127.0.0.1:8000/docs

## Testes

Para executar os testes automatizados e verificar a integração da Tool de cálculo: 
pytest 

## Arquitetura
O projeto segue uma estrutura Package by Feature para facilitar a manutenção e escalabilidade.
app/
├── main.py              # Entrypoint e Global Exception Handlers
├── chat/                # Feature: Chat
│   ├── router.py        # Endpoint e documentação Swagger
│   ├── service.py       # Regra de negócio
│   ├── schemas.py       # Validação Pydantic (Input/Output)
│   └── agent/           # Camada de IA
│       ├── core.py      # Configuração do Agente Strands
│       └── tools.py     # Tool de Calculadora
└── tests/               # Testes de integração


