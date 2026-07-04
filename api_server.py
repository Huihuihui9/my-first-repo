from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="学习练习API", version="0.1.0")


class CalcRequest(BaseModel):
    a: float
    b: float
    op: str


@app.get("/")
def root():
    return {"message": "Hello! This is my first API."}


@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}!"}


@app.post("/calc")
def calculate(req: CalcRequest):
    if req.op == "+":
        result = req.a + req.b
    elif req.op == "-":
        result = req.a - req.b
    elif req.op == "*":
        result = req.a * req.b
    elif req.op == "/":
        if req.b == 0:
            return {"error": "cannot divide by zero"}
        result = req.a / req.b
    else:
        return {"error": f"unsupported operator: {req.op}"}

    return {"expression": f"{req.a} {req.op} {req.b}", "result": result}
