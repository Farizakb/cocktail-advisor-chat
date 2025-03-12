# app/main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.routes import router as chat_router

app = FastAPI()

# Mount the directory for static files (JavaScript, CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure the templates directory for HTML files
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Include chat endpoints under a common prefix
app.include_router(chat_router, prefix="/api")
