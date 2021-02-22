
from typing import Optional, List
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Response, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .library.helpers import openfile


app = FastAPI()
templates = Jinja2Templates(directory = 'templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/', response_class = HTMLResponse)
async def home(request : Request) :
    data= {
        'page' : 'Home page'
    }
    return templates.TemplateResponse('page.html',
                                    context = {'request': request, 'data':data})

@app.get('/page/{page_name}', response_class = HTMLResponse)
async def page(request: Request, page_name: str):
    
    data = openfile(page_name+'.md')
    # data = {
    #     'page': page_name
    # }
    return templates.TemplateResponse('page.html',
                                    context = {'request': request, 'data':data})
