from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from chat.router import router as chat_router
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(
    title="API de Chat com Agente IA",
    description="""Desafio Técnico - Integração FastAPI + Ollama + Strands para criação de um agente de chat inteligente.""",
    version="1.0.0"
)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500, 
        content={
            "tipo_erro": type(exc).__name__,
            "mensagem": str(exc),
            "nota": "Ocorreu um erro interno no servidor."
        },
        media_type="application/problem+json"
    )

from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "tipo_erro": "ErroValidacao",
            "mensagem": "Os dados enviados estão ausentes.",
            "detalhes": exc.errors(), 
            "nota": f"Erro de validação na rota {request.url.path}"
        },
        media_type="application/problem+json"
    )
app.include_router(chat_router, prefix="/api") 
