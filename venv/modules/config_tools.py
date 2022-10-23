# Path: venv\modules\config_tools.py
from dataclasses import dataclass
import toml


_database = toml.load("config/config.toml")["database"]
_surreal_server = toml.load("config/config.toml")["servers"]["SurrealDB"]


@dataclass
class BuiltDatabaseConfig():
    host:str= _surreal_server["host"] 
    port:str= _surreal_server["port"]
    namespace:str= _database["namespace"]
    database:str= _database["database"]
    enabled:str= _database["enable"]
    db_type:str= _database["db_type"]
    username:str= _database["user"]                            
    password:str= _database["password"]
    url:str= f"http://{host}:{port}/sql"