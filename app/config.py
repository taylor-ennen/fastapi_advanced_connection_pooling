from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

## SURREAL DATABASE
DATABASE_URL="postgresql://postgres:password@localhost:8082/something" 
SURREAL_DB ="root:root@localhost:8082/sql"
# This is the database that I want to connect to

engine=create_engine(SURREAL_DB, echo=True)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
