import fastapi
import uvicorn

api = fastapi.FastAPI()
print("hello fast api")


@api.get("/api/calculate")
def sum():
    value = 2 + 2
    return {"value": value}


uvicorn.run(api, port=80)