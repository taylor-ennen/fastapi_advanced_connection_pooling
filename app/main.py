from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def Main():
    return "Welcome to the Something API"
