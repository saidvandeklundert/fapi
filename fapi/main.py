import fastapi
from starlette.requests import Request
import uvicorn
from typing import Optional
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

api = fastapi.FastAPI()
templates = Jinja2Templates("templates")
api.mount("/static", StaticFiles(directory="static"), name="static")
# swagger
# http://127.0.0.1/docs

# http://127.0.0.1/
@api.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# http://127.0.0.1/api/number
@api.get("/api/number")
def give_number():
    value = 2 + 2
    return {"value": value}


# http://127.0.0.1/api/calculate?x=2&y=8
# http://127.0.0.1/api/calculate?x=2&y=8&z=10
@api.get("/api/calculate")
def sum(x: int, y: int, z: Optional[int] = None):
    if z and z == 20:
        return fastapi.Response(
            content='{ "error" : "ERROR: z cannot be 20"}',
            media_type="application/json",
            status_code=400,
        )
    elif z and z == 30:
        return fastapi.responses.JSONResponse(
            content={"error": "ERROR: z cannot be 30"}, status_code=400
        )

    ret = {"x": x, "y": y, "z": z}
    value = x + y
    if z:
        value += z
    ret["value"] = value
    return ret


uvicorn.run(api, port=80, host="0.0.0.0")
