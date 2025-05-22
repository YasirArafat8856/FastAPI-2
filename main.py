from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    x = 3
    y = 2
    if x > y:
        return {"1st": "Hello, python World! " + str(x + y)+" "+ str(type(x))}
    else:
        return {"2nd": "Hello, python World! " + str(x - y)}
