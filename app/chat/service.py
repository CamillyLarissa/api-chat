import json

from fastapi import HTTPException
from chat.schemas import Response
from chat.llm.agent import create_ollama_agent

def create_message(message: str) -> str:

    agent = create_ollama_agent()

    response_obj = agent.structured_output(Response, message)

    return response_obj.response