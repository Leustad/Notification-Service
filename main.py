import uvicorn
from fastapi import FastAPI

from routes.healthcheck import healthcheck_router
from routes.remind.remind import remind_router

app = FastAPI()


app.include_router(remind_router)
app.include_router(healthcheck_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=33510, reload=True)
