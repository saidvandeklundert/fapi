import fastapi
import uvicorn

from starlette.staticfiles import StaticFiles
from views import home
from api import math_and_numbers
from api import strings_and_stuff
from fastapi import BackgroundTasks

api = fastapi.FastAPI()


def configure():
    configure_routing()


def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(math_and_numbers.router)
    api.include_router(strings_and_stuff.router)
    api.include_router(home.router)


# swagger
# http://127.0.0.1/docs


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@api.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=80, host="0.0.0.0")
