
from os import path

import asyncio

import asyncio

from growler import (App, create_http_server)
from growler.middleware import (Logger, Static, Renderer)

app = App('GrowlerServer')

this_dir = path.dirname(__file__)

app.use(Logger())
app.use(Renderer(path.join(this_dir, "views"), "jade"))

@app.get('/')
def index(req, res):
    res.render("home")

@app.get('/hello')
def hello_world(req, res):
    res.send_text("Hello World!!")

http = create_http_server(app, host='127.0.0.1', port=8000)
asyncio.get_event_loop().run_until_complete(http.listen())
