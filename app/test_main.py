
from typing import Optional, List
from fastapi import FastAPI, Response, Form

from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
# import uvicorn

from enum import Enum

# from common.config import conf
from pydantic.main import BaseModel

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

class Item(BaseModel) :
    name: Optional[str] = None
    age: Optional[int] = None
    tag: List[str] = []

items = {
    'foo' : {'name':'Foo','age':'50'},
    'bar' : {'name':'Bar','age':'20','tag':['aa','ab']}
}

app = FastAPI()


@app.post("/items/")
async def create_item(item : Item):
    item_dict = item.dict()
    if item.tax :
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

@app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item):
    return {'item_id':item_id, **item.dict()}



# @app.get("/items/{item_id}", response_model = Item)
# async def read_item(item_id: str):
#     return items[item_id]

# @app.put("/items/{item_id}", response_model = Item)
# async def update_item(item_id: str, item: Item) :
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {'username' : username}

@app.get("/index/")
def get_html_data1():
    html_content = """
    <form method="post">
    <div class="container">
        <label for="uname"><b>Username</b></label>
        <input type="text" placeholder="Enter Username" name="uname" required>

        <label for="psw"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" name="psw" required>

        <button type="submit">Login</button>
        <label>
        <input type="checkbox" checked="checked" name="remember"> Remember me
        </label>
    </div>

    <div class="container" style="background-color:#f1f1f1">
        <button type="button" class="cancelbtn">Cancel</button>
        <span class="psw">Forgot <a href="#">password?</a></span>
    </div>
    </form>
    """
    return HTMLResponse(content=html_content, status_code = 200)


@app.get("/tttt/")
def get_html_data():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <img src="https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile7.uf.tistory.com%2Fimage%2F24283C3858F778CA2EFABE">
            click
            </a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code = 200)


@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {"file_path": file_path} 

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName) :
    if model_name == ModelName.alexnet :
        msg = 'deep ftw'
    elif model_name.value == 'lenet' :
        msg = 'LeCNN'
    else :
        msg = 'resi'

    return f'model name : {model_name}, msg : {msg}'

@app.get(path="/kang")
async def hello():
    return {'강혜민 바보'}


@app.get(path="/")
async def hello():
    return 'hello world'

@app.get(path="/hello/query")
async def hello_with_querystring(name:str) :
    return f'hello with name, your name is {name} (1111)'

@app.get(path="/hello/post")
async def hello_post(request : Item) :
    return f'hello with name, your name is {name}, age {age}'
