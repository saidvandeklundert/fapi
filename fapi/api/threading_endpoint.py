import fastapi
from concurrent.futures import ThreadPoolExecutor
from fastapi import BackgroundTasks
import time


router = fastapi.APIRouter()

"""
curl -X 'POST' \
"http://127.0.0.1/api/threading/background/show%20running-config" \
-H 'accept: application/json'   -d ''
"""


@router.post("/api/threading/background/{word}")
async def backgroundword(word: str, background_tasks: BackgroundTasks):
    print("starting background task:")
    background_tasks.add_task(back_ground_func, word)
    return f"words are being written in the background"


def back_ground_func(word: str):
    futures = threading(word)

    for item in futures:
        print(item)


def io_bound_function(host: str, word: str):
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(f"io_bound_function called with argument {word}")
    time.sleep(3)
    with open("/var/log/log.txt", mode="a") as words_file:
        content = f"{host}: command {word}\n"
        words_file.write(content)
    print(f"io_bound_function with argument {word} ended")
    return True


def threading(word: str):
    futures = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        host_list = ["r1 ", "r2 ", "r3 ", "r4", "r5 ", "r6"]
        for host in host_list:
            futures.append(executor.submit(io_bound_function, host, word))

    return futures