import fastapi
import uvicorn

api = fastapi.FastAPI()
print("hello fast api")


@api.get("/api/number")
def give_number():
    value = 2 + 2
    return {"value": value}


@api.get("/api/calculate")
def sum(x, y):
    value = x + y
    return {"value": value}


uvicorn.run(api, port=80, host="0.0.0.0")
