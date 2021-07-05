import fastapi
from fastapi import BackgroundTasks
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio


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
    futures = example_threadpool()
    s = ""
    for item in futures:
        s += item.result()
    with open("/var/log/log.txt", mode="w") as words_file:
        content = f"{words} {s}"
        words_file.write(content)


def io_bound_function(parameter):
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(f"io_bound_function called with argument {parameter}")
    time.sleep(3)
    print(f"io_bound_function with argument {parameter} ended")
    return parameter


def example_threadpool():
    """
    Example where a function that requires an arg
     is passed to a ThreadPoolExecutor.
    In this case, the 'max_workers' is configurable.
    """

    futures = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        argument_list = ["this ", "will ", "appear ", "in ", "the ", "log"]
        for argument in argument_list:
            futures.append(executor.submit(io_bound_function, argument))

    return futures