from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            # Read input values
            savings = data.get("savings", 0)
            goal = data.get("goal", "")
            scheme = data.get("scheme", "")

            # Simple logic
            if savings < 200000:
                color = "red"
                tip = "You need to save more."
            elif savings < 500000:
                color = "orange"
                tip = "You're getting closer!"
            else:
                color = "green"
                tip = "You're financially ready."

            # Return result
            result = {"color": color, "tip": tip}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
