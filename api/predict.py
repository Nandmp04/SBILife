from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        savings = int(data.get("savings", 0))
        goal = data.get("goal", "").lower()
        scheme = data.get("scheme", "").lower()

        if savings >= 500000:
            color = "green"
            tip = "You're financially ready."
        elif savings >= 200000:
            color = "orange"
            tip = "You may need to save more."
        else:
            color = "red"
            tip = "Savings too low for this goal."

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"color": color, "tip": tip}).encode())
