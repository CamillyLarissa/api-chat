import math

from strands import tool

@tool
def calculator(expressao: str):
    """
    Calcula expressões matemáticas simples.
    Suporta: +, -, *, /, ** (potência) e funções básicas (sin, cos, sqrt).
    """
    funcoes_permitidas = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "log": math.log,
        "pi": math.pi,
        "e": math.e,
        "abs": abs,
        "round": round
    }

    try:
        resultado = eval(expressao, {"__builtins__": None}, funcoes_permitidas)
        return str(resultado)
    
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"
