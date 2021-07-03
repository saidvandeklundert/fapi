"""
in main:
    from api import multiplications
    api.include_router(multiplications.router)
in here:
    import fastapi
    router = fastapi.APIRouter()
"""
import fastapi
from typing import Optional

router = fastapi.APIRouter()


# http://127.0.0.1/api/number
@router.get("/api/number")
def give_number():
    value = 2 + 2
    return {"value": value}


# http://127.0.0.1/api/calculate?x=2&y=8
# http://127.0.0.1/api/calculate?x=2&y=8&z=10
@router.get("/api/calculate")
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
