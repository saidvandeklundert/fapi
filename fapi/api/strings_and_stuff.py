import fastapi
from fastapi import BackgroundTasks
import time
import asyncio
from pydantic import BaseModel

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


# http://127.0.0.1/api/words/backgroundword/backgroundtask
@router.post("/api/words/backgroundword/{words}")
async def backgroundword(words: str, background_tasks: BackgroundTasks):

    background_tasks.add_task(background_word, words)
    return f"words are being written in the background"


def background_word(words: str):
    with open("/var/log/log.txt", mode="w") as words_file:
        content = f"{words}"
        words_file.write(content)
    time.sleep(30)
