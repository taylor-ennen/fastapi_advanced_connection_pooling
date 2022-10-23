
import httpx
import json
from main import free_db_clients
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder as jencoder
from fastapi.templating import Jinja2Templates
from modules.config_tools import BuiltDatabaseConfig
from datetime import datetime
from typing import Union

db_params = BuiltDatabaseConfig

templates = Jinja2Templates(directory="templates")

class PydanticResspone(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


async def db(q):
    try:
        db_client = free_db_clients.pop() if len(
            free_db_clients) else httpx.AsyncClient(headers={"Temporal": "Yes"})
        res = await db_client.post(url=f"{db_params.url}/", auth=(f"{db_params.username}, {db_params.password}"), data=q)
        if "Temporal" not in str(db_client.headers):
            free_db_clients.append(db_client)
        else:
            db_client.aclose()
        res = json.loads(res.content)
        return res[-1]
    except Exception as exc:
        status_code = exc.statuscode if hasattr(exc, "status_code") else 500
        detail = exc.detail if hasattr(
            exc, "detail") else "Internal Server Error"
        return JSONResponse(status_code=status_code, content={"detail": detail})
    finally:
        pass
