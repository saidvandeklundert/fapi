import fastapi
from fastapi import BackgroundTasks
import time
import asyncio
from pydantic import BaseModel

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


# http://127.0.0.1/api/words/backgroundword/backgroundtask
@router.post("/api/words/backgroundword/backgroundtask")
async def backgroundword(
    word: str, second_word: str, background_tasks: BackgroundTasks
):

    background_tasks.add_task(background_word, word)
    return f"{word} 2nd word {second_word}"


def long_running(x):
    print(f"sleep for {x} seconds")
    time.sleep(x)
    print("done sleeping")


class Params(BaseModel):
    sleep_time: int


# http://127.0.0.1/api/words/words/bgtask/
@router.post("/api/words/bgtask/")
def start_long_running(p: Params, bg_task: BackgroundTasks):
    bg_task.add_task(long_running, p.sleep_time)
    return {"message": "Queued task."}
