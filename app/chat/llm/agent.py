from strands import Agent
from chat.llm.tools import calculator
from strands.models.ollama import OllamaModel
from dotenv import load_dotenv
import os


def setup_environment():
    
    load_dotenv()

    ollama_host_url = os.getenv('STRANDS_OLLAMA_HOST')
    model = os.getenv('STRANDS_OLLAMA_MODEL')

    if not ollama_host_url or not model:
        raise ValueError("STRANDS_OLLAMA_HOST and STRANDS_OLLAMA_MODEL é necessário nas variáveis de ambiente.")

    return ollama_host_url, model

def create_ollama_agent():
    
    host_url, model_name = setup_environment()
    ollama_model = OllamaModel(
        host=host_url,
        model_id=model_name
    )

    agent = Agent(tools=[calculator], model=ollama_model)

    return agent



