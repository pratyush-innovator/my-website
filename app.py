import http.server
import socketserver
import os

PORT = 8000
log_path = os.path.join(os.getcwd(), "traffic_log.txt")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        with open(log_path, "a") as f:
            f.write(f"{self.address_string()} - {format % args}\n")
        super().log_message(format, *args)

    def do_GET(self):
        # Agar tum /admin type karoge, toh data dikhega
        if self.path == '/admin':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # File se data read karo
            if os.path.exists(log_path):
                with open(log_path, "r") as f:
                    data = f.read().replace('\n', '<br>')
                self.wfile.write(f"<h1>Traffic Data</h1><p>{data}</p>".encode())
            else:
                self.wfile.write(b"<h1>No data yet!</h1>")
        else:
            # Baaki sab normal website dikhaye
            super().do_GET()

Handler = MyHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server chal raha hai! Data yahan dekho: http://localhost:8000/admin")
    httpd.serve_forever()