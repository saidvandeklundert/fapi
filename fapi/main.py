import fastapi
import uvicorn

api = fastapi.FastAPI()
print("hello fast api")


def sum():
    return 2 + 2


uvicorn.run(api)