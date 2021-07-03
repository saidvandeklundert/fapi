import fastapi
import uvicorn

api = fastapi.FastAPI()
print("hello fast api")


@api.get("/api/calculate")
def sum():
    return 2 + 2


uvicorn.run(api, port=80)