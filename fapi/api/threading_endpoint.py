import fastapi
from concurrent.futures import ThreadPoolExecutor
from fastapi import BackgroundTasks
import time


router = fastapi.APIRouter()


# http://127.0.0.1/api/threading/background/word
@router.post("/api/threading/background/{words}")
async def backgroundword(words: str, background_tasks: BackgroundTasks):
    print("starting background task:")
    background_tasks.add_task(background_word, words)
    return f"words are being written in the background"


def background_word(words: str):
    futures = example_threadpool()
    s = ""
    for item in futures:
        s += item.result()
    with open("/var/log/log.txt", mode="a") as words_file:
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