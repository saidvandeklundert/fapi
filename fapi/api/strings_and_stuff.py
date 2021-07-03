import fastapi

router = fastapi.APIRouter()


# http://127.0.0.1/api/words/upper/{word}
@router.get("/api/words/upper/{word}")
def upper(word: str):
    return f"your word in uppercase: {word.upper()}"


# http://127.0.0.1/api/words/word/{word}
@router.get("/api/words/word/{word}")
def word(word: str, second_word: str = "default"):
    return f"{word} 2nd word {second_word}"