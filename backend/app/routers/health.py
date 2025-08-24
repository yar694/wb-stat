from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Health check")
def root():
    return {"status": "ok"}