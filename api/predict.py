from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body)

        savings = data.get("savings", 0)
        if savings < 200000:
            color = "red"
            tip = "Save more"
        elif savings < 500000:
            color = "orange"
            tip = "Almost there"
        else:
            color = "green"
            tip = "You're ready!"

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"color": color, "tip": tip}).encode())
