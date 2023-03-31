
from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

class UserInput(BaseModel):
    operation: str
    x: float
    y: float

app = FastAPI()

@app.post("/calculate")
def operate(user_input: UserInput):
    print(f'user_input: {user_input}')
    result = calculate(user_input.operation, 
                user_input.x, 
                user_input.y)

    return {"result": result}

