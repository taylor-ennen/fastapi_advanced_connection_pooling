import uuid
from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
import saucey


router = APIRouter()


@router.get("/", response_class=Response)
async def foo(request: Request):
    items = await saucey.db("SELECT * FROM items")
    return Response(content=items, media_type="application/json")
