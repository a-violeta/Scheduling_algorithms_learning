from fastapi import FastAPI
from routers.scheduling import router as scheduling_router

app = FastAPI()
app.include_router(scheduling_router)

@app.get("/")
def home():
    return {"status": "server running"}
