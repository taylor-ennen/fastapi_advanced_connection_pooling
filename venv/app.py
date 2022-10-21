from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_home():
    return {"info": "Welcome to the Something API"}
