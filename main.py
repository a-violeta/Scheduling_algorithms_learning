from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from fastapi.responses import FileResponse
from fastapi import Request
from fastapi import FastAPI
from routers.scheduling import router as scheduling_router
from database import Base, engine
from routers import exercise

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(scheduling_router)
app.include_router(exercise.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/exercise/{exercise_id}")
def exercise_page(request: Request, exercise_id : int):
    return templates.TemplateResponse("exercise.html", {"request": request, "exercise_id": exercise_id})