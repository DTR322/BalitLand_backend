from fastapi.openapi.docs import get_swagger_ui_html
from app.students.router import router as router_students
from app.teachers.router import router as router_teachers

from fastapi import FastAPI

app = FastAPI(
    title="Мой API",
    description="Описание моего API",
    version="1.0.0",
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html_cdn():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        # swagger_ui_dark.css CDN link
        swagger_css_url="https://cdn.jsdelivr.net/gh/Itz-fork/Fastapi-Swagger-UI-Dark/assets/swagger_ui_dark.min.css"
    )


@app.get("/")
def home_page():
    return {"message": "Главная"}


app.include_router(router_students)
app.include_router(router_teachers)
