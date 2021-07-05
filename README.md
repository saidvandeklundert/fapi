Playing with fast API



```
docker run --name='fastapi' --hostname='fastapi' -p 80:80 -di centos /bin/sh
docker start 0db0781dc5ff
docker exec -it 0db0781dc5ff /bin/sh
yum install python39
python3 -m venv fapi
source /fapi/bin/activate
which python
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```


Minimal API:
```python
import fastapi
import uvicorn

api = fastapi.FastAPI()
print("hello fast api")


@api.get("/api/calculate")
def sum():
    value = 2 + 2
    return {"value": value}

uvicorn.run(api, port=80, host="0.0.0.0")
```

Input validation example:

```python
from pydantic.error_wrappers import ValidationError


class ValidationError(Exception):
    def __init__(self, error_msg: str, status_code: int):
        super().__init__(error_msg)
        self.status_code = status_code
        self.error_msg = error_msg

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
```


Background task:

```python
from fastapi import BackgroundTasks
@router.post("/api/words/backgroundword/{words}")
async def backgroundword(words: str, background_tasks: BackgroundTasks):

    background_tasks.add_task(background_word, words)
    return f"words are being written in the background"


def background_word(words: str):
    time.sleep(30)
    with open("/var/log/log.txt", mode="w") as words_file:
        content = f"{words}"
        words_file.write(content)

# https://github.com/tiangolo/fastapi/blob/master/docs/en/docs/tutorial/background-tasks.md
# https://www.starlette.io/background/
```