import fastapi

router = fastapi.APIRouter()


# http://127.0.0.1/api/words/upper/{word}
@router.get("/api/words/upper/{word}")
def upper(word: str):
    return word.upper()
