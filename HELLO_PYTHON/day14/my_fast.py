from fastapi import FastAPI
from fastapi.params import Form
from pydantic.main import BaseModel
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
import uvicorn

from day11.daomember import DaoMember
from starlette.templating import Jinja2Templates
from day11 import daomember


templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class Member(BaseModel):
    m_id : str    =None
    m_name : str  =None
    tel : str     =None
    email : str    =None
    
@app.get("/",response_class=HTMLResponse)
async def root (request: Request):
    return RedirectResponse(url="/static/member.html")

@app.post("/member_select")
def member_select(m: Member):
    print(m)
    de = DaoMember()
    list = de.selectList()
    return {"list" : list}

@app.post("/member_select_one")
def member_select_one(m: Member):
    memberId = m.m_id
    de = DaoMember()
    member = de.selectOne(memberId)
    print(member)
    return {"member" : member}

@app.post("/member_insert")
def member_insert(m: Member):
    de = DaoMember()
    cnt = de.insert(m.m_id, m.m_name, m.tel, m.email)
    return {"cnt" : cnt}

@app.post("/member_update")
def member_update(m: Member):
    de = DaoMember()
    cnt = de.update(m.m_id, m.m_name, m.tel, m.email)
    return {"cnt" : cnt}

@app.post("/member_delete")
def member_delete(m: Member):
    de = DaoMember()
    cnt = de.delete(m.m_id)
    return {"cnt" : cnt}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)