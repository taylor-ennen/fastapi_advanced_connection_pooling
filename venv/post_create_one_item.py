from calendar import c
import uuid
from fastapi import APIRouter, Form, Response
import saucey


router = APIRouter()


@router.post("/items")
async def create_item(item_name: str = Form(""), item_description: str = Form("")):
    item_id = str(uuid.uuid4()).replace("-", "")
    query = f"""LET $item_id = {item_id};
    LET $item_name = {item_name};
    LET $item_description = {item_description};
    CREATE items SET key = $item_id, name = $item_name, description = $item_description"""
    res = await saucey.db(q=query)
    res = saucey.jencoder(res)
    return Response(content=res, media_type="application/")
