import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except:
        return False

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hbbs = check_port("hbbs", 21116)
        hbbr = check_port("hbbr", 21117)

        if hbbs and hbbr:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(503)
            self.end_headers()
            self.wfile.write(
                f"hbbs={hbbs} hbbr={hbbr}".encode()
            )

    def log_message(self, *args):
        pass

HTTPServer(("0.0.0.0", 22116), Handler).serve_forever()