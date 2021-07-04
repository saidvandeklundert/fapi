import fastapi
from fastapi import BackgroundTasks
import time
import asyncio

router = fastapi.APIRouter()


def background_word(word: str):
    print(word)
    time.sleep(8)


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


# http://127.0.0.1/api/words/backgrounword/{word}?second_word=secondword
@router.post("/api/words/backgrounword/{word}")
async def backgrounword(word: str, second_word: str, background_tasks: BackgroundTasks):

    background_tasks.add_task(background_word, word)
    return f"{word} 2nd word {second_word}"
