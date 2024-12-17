from fastapi import FastAPI
from app.students.router import router as router_students
from app.teachers.router import router as router_teachers

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Главная"}


app.include_router(router_students)
app.include_router(router_teachers)
