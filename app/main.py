from app.students.router import router as router_students
from app.teachers.router import router as router_teachers


from fastapi import FastAPI

app = FastAPI(
    title="Мой API",
    description="Описание моего API",
    version="1.0.0",
)


@app.get("/")
def home_page():
    return {"message": "Главная"}


app.include_router(router_students)
app.include_router(router_teachers)

