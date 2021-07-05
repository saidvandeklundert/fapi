import fastapi
import uvicorn

from starlette.staticfiles import StaticFiles
from views import home
from api import math_and_numbers
from api import strings_and_stuff
from api import threading_endpoint

api = fastapi.FastAPI()


def configure():
    configure_routing()


def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(math_and_numbers.router)
    api.include_router(strings_and_stuff.router)
    api.include_router(home.router)
    api.include_router(threading_endpoint.router)


# swagger
# http://127.0.0.1/docs


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=80, host="0.0.0.0")
