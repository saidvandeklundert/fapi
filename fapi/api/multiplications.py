"""
in main:
    from api import multiplications
    api.include_router(multiplications.router)
in here:
    import fastapo
    router = fastapi.APIRouter()
"""
import fastapi

router = fastapi.APIRouter()


# http://127.0.0.1/api/multiplications/multiplication
@router.get("/api/multiplications/multiplication")
def give_number():
    value = 2 + 2
    return {"value": value}
