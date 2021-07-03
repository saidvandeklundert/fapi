import fastapi

router = fastapi.APIRouter()


# http://127.0.0.1/api/multiplication
@router.get("/api/multiplication")
def give_number():
    value = 2 + 2
    return {"value": value}
