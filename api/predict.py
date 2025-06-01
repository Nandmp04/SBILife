from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        savings = data.get("savings", 0)
        goal = data.get("goal", "")
        scheme = data.get("scheme", "")

        # Sample logic
        color = "green" if savings > 500000 else "orange"
        tip = "Great!" if color == "green" else "Save more."

        response = {"color": color, "tip": tip}

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
