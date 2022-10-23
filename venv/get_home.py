from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_home():
    return {"info": "Welcome to the Something API"}








