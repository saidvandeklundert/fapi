Playing with fast API



```
docker run --name='fastapi' --hostname='fastapi' -p 80:80 -di centos /bin/sh
docker start 0db0781dc5ff
docker exec -it 0db0781dc5ff /bin/sh
yum install python39
python3 -m venv fapi
. fapi/bin/activate
source fapi/bin/activate
which python
python3 -m pip install --upgrade pip
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