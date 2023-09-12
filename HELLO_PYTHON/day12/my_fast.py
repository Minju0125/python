from fastapi import FastAPI
import uvicorn
from starlette.responses import HTMLResponse
from fastapi.params import Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def forw(request: Request):
    return templates.TemplateResponse("forw.html", {"request":request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)