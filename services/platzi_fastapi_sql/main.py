# Python standard library

# FastAPI
from fastapi import FastAPI

# Databases
from models import metadata
from config import engine, database

metadata.create_all(engine)

api = FastAPI()

@api.on_event("startup")
async def startup():
    await database.connect()

@api.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@api.get("/")
async def hello():
    return {"message": "Hello World"}
