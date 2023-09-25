import uvicorn
from fastapi import FastAPI

from routes.remind import remind_router

app = FastAPI()

app.include_router(remind_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
