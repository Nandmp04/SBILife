from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            savings = data.get("savings", 0)
            goal = data.get("goal", "")
            scheme = data.get("scheme", "")

            # Simple logic
            color = "green" if savings > 500000 else "orange"
            tip = "You're on track!" if color == "green" else "Consider saving more."

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"color": color, "tip": tip}).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_msg = {"error": str(e)}
            self.wfile.write(json.dumps(error_msg).encode())
