# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     x = 3
#     y = 2
#     if x > y:
#         return {"1st": "Hello, python World! " + str(x + y)+" "+ str(type(x))}
#     else:
#         return {"2nd": "Hello, python World! " + str(x - y)}


from fastapi import FastAPI
from . import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(routes.router)
