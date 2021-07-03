import fastapi
import uvicorn

api = fastapi.FastAPI()
print("hello fast api")

# http://127.0.0.1/api/number
@api.get("/api/number")
def give_number():
    value = 2 + 2
    return {"value": value}


# http://127.0.0.1/api/calculate?x=2&y=8
@api.get("/api/calculate")
def sum(x: int, y: int, z: Optional[int] = None):
    value = x + y
    if z:
        value += z
    return {"value": value}


uvicorn.run(api, port=80, host="0.0.0.0")
