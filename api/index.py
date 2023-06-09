import os
from sanic import Sanic, response
from dotenv import load_dotenv
load_dotenv()

ex = os.environ.get("EXAMPLE_ENV")
print(ex)

app: Sanic = Sanic("app_name")

# @app.route("/")
# async def home(request):
#    return response.text("Hello Sanic")
 
# @app.route('/')
# @app.route('/<path:path>')
# async def index(request, path=""):
#     return response.json({'hello': path})

@app.get('/api/example')
async def example(request):
    return response.json({"hello": "world"})


# NON SANIC APPROACH
# from http.server import BaseHTTPRequestHandler
# import re
# import json

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         print(f"Path: {self.path}")
#         text = "Hello, world!"
#         if re.search('/api/example/*', self.path):
#             text = json.dumps({"hello": "world"})
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write(text.encode('utf-8'))
#         return