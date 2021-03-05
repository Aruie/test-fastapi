
from typing import Optional, List
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Response, Form, Request, WebSocket

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .library.helpers import openfile


import socket
ip_address = socket.gethostbyname(socket.gethostname())

app = FastAPI()
templates = Jinja2Templates(directory = 'templates')
app.mount('/static', StaticFiles(directory='static'), name='static')



main_html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1 id="id_h0">WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button onclick="aleartDialogBox()">Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:7500/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            };
            
            function aleartDialogBox() {
                // alert("aaaaa")
                var str = document.getElementById("id_h0")
                str.innerHTML = "후후후후후"
            };

            console.log(4*5);
        
        </script>
    </body>
</html>
"""

main_html = main_html.replace('localhost',ip_address)
# main_html = main_html.replace('localhost','127.0.1.1')




@app.get(path="/")
async def hello():
    # return 'hello world'
    return HTMLResponse(main_html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
    


# @app.get('/', response_class = HTMLResponse)
# async def home(request : Request) :
#     data= {
#         'page' : 'Home page'
#     }
#     return templates.TemplateResponse('page.html',
#                                     context = {'request': request, 'data':data})

@app.get('/page/{page_name}', response_class = HTMLResponse)
async def page(request: Request, page_name: str):
    
    data = openfile(page_name+'.md')
    # data = {
    #     'page': page_name
    # }
    return templates.TemplateResponse('page.html',
                                    context = {'request': request, 'data':data})
