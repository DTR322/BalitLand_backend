from fastapi import FastAPI

import os

from app.models import student

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Главная"}