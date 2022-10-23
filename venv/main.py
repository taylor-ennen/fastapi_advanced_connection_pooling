from fastapi import FastAPI
from httpx import AsyncClient
from fastapi import FastAPI
from modules.config_tools import BuiltDatabaseConfig
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

db_config = BuiltDatabaseConfig


#? \U0001F4BC clients
AsyncClientSpawner = AsyncClient(headers={"Content-Type": "application/json", "ns": db_config.namespace, "db": db_config.database,})
db_clinet_one=AsyncClientSpawner
db_clinet_two=AsyncClientSpawner
#? \U0001F3CA\U0000200D\U00002642\U0000FE0F pools
free_db_clients=[db_clinet_one,db_clinet_two]

#? \U0001F69C routes
import get_home
app.include_router(get_home.router)

import post_create_one_item
app.include_router(post_create_one_item.router)

import get_all_items
app.include_router(get_all_items.router)

