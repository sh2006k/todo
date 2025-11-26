import json
from http.server import BaseHTTPRequestHandler, HTTPServer

def read_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

class SimpleServer(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length"))
        body = self.rfile.read(length)
        data = json.loads(body)

        # LOGIN
        if self.path == "/login":
            users = read_json("users.json")
            for u in users:
                if u["username"] == data.get("username") and u["password"] == data.get("password"):
                    self._set_headers(200)
                    self.wfile.write(json.dumps({"message": "login ok"}).encode())
                    return

            self._set_headers(401)
            self.wfile.write(json.dumps({"message": "invalid login"}).encode())
            return

        # ADD TODO
        if self.path == "/todos":
            todos = read_json("todos.json")
            new_todo = {"id": len(todos) + 1, "text": data.get("text")}
            todos.append(new_todo)
            write_json("todos.json", todos)

            self._set_headers(200)
            self.wfile.write(json.dumps(new_todo).encode())
            return

    def do_GET(self):
        if self.path == "/todos":
            todos = read_json("todos.json")
            self._set_headers(200)
            self.wfile.write(json.dumps(todos).encode())
            return

# START SERVER
print("Server running on http://127.0.0.1:5001")
server = HTTPServer(("127.0.0.1", 5001), SimpleServer)
server.serve_forever()

