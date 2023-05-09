from http.server import BaseHTTPRequestHandler
import re
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(f"Path: {self.path}")
        text = "Hello, world!"
        if re.search('/api/example/*', self.path):
            text = json.dumps({"hello": "world"})
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(text.encode('utf-8'))
        return
