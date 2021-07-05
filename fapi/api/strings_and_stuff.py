import fastapi
import time
import asyncio
from models.errors import ValidationError

router = fastapi.APIRouter()

# http://127.0.0.1/api/words/upper/{word}
@router.get("/api/words/upper/{word}")
def upper(word: str):
    return f"your word in uppercase: {word.upper()}"


# To display the default:
# http://127.0.0.1/api/words/word/{word}
# To supply a value other then the default:
# http://127.0.0.1/api/words/word/{word}?second_word=secondword
@router.get("/api/words/word/{word}")
def word(word: str, second_word: str = "default"):
    time.sleep(8)
    return f"{word} 2nd word {second_word}"


# http://127.0.0.1/api/words/asyncword/{word}?second_word=secondword
@router.get("/api/words/asyncword/{word}")
async def asyncword(word: str, second_word: str = "default"):
    await asyncio.sleep(2)
    return f"{word} 2nd word {second_word}"


# http://127.0.0.1/api/words/correctword/{word}
@router.get("/api/words/correctword/{word}")
def correctword(word: str):
    word = validate_word(word)
    try:
        return f"{word}"
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as err:
        return fastapi.Response(
            content=f"ERROR PROCESSING YOUR REQUEST {err}", status_code=500
        )


def validate_word(word: str) -> str:

    if word != "proper_word":
        error = f"Invalid word: {word}. It must be 'proper_word'"
        raise ValidationError(status_code=400, error_msg=error)

    return word