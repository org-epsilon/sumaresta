from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de Suma")

# Permite conectar la interfaz web con el backend de Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def sumar(a: float, b: float) -> float:
    return a + b

@app.get("/api/sumar")
def api_sumar(num1: float, num2: float):
    resultado = sumar(num1, num2)
    return {
        "num1": num1,
        "num2": num2,
        "resultado": resultado,
        "mensaje": f"La suma de {num1} y {num2} es: {resultado}"
    }