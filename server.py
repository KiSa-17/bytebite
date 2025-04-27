from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs
from relog import register, login
from database import new_med_detail
from jwtreq import decode_token

class mycare Handler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _parse_post(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body)

    def do_POST(self):
        if self.path == '/register':
            data = self._parse_post()
            response, status = register(data)
            self._set_headers(status)
            self.wfile.write(json.dumps(response).encode())

        elif self.path == '/login':
            data = self._parse_post()
            response, status = login(data)
            self._set_headers(status)
            self.wfile.write(json.dumps(response).encode())

        elif self.path == '/add_medication':
            auth_header = self.headers.get('Authorization')
            if not auth_header:
                self._set_headers(401)
                self.wfile.write(json.dumps({"message": "Missing Token"}).encode())
                return

            token = auth_header.split(" ")[1]
            user_id = decode_token(token)
            if not user_id:
                self._set_headers(401)
                self.wfile.write(json.dumps({"message": "Invalid Token"}).encode())
                return

            data = self._parse_post()
            newmed(user_id, data['name'], data['dosage'], data['frequency'], data['time_of_day'])
            self._set_headers(201)
            self.wfile.write(json.dumps({"message": "Medication added"}).encode())

def run(server_class=HTTPServer, handler_class=MediBuddyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running at http://localhost:{port}')
    httpd.serve_forever()

if _name_ == "_main_":
    run()
