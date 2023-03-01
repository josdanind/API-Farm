# Python standard library

# FastAPI
from fastapi import FastAPI


api = FastAPI()

@api.get("/")
async def hello():
    return {"message": "Hello World"}
