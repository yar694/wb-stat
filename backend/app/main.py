from fastapi import FastAPI
from .routers import health, ads
from .config import settings

app = FastAPI(title=settings.app_name, version="0.1.0")

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(ads.router, prefix="/wb", tags=["wildberries"])

# Запуск через: uvicorn app.main:app --app-dir backend --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)