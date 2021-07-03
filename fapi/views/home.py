import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates("templates")
# http://127.0.0.1/
@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/ma_face.jpeg")