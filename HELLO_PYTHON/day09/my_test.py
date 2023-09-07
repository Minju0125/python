from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return "Hello World"

@app.get("/param", response_class=HTMLResponse)
async def param(menu: str):
    print("menu", menu)
    return "param : " + menu

@app.post("/post", response_class=HTMLResponse)
async def post(menu: str = Form(...)):
    print("menu :" , menu )
    return "post : " + menu

@app.get("/forw", response_class=HTMLResponse)
async def forw(request: Request):
    a = '홍길동'
    b = ['베어그릴스', '솔로지옥', '정글의법칙']
    c = [
        {'e_id': 1, 'e_name': '1', 'gen': '1', 'addr': '1'},
        {'e_id': 2, 'e_name': '2', 'gen': '2', 'addr': '2'} 
        ]
    return templates.TemplateResponse("forw.html",{"request":request, "a":a, "b":b, "c":c})
    return "Hello World"

if __name__ =="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)