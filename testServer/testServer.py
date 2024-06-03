from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.content)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        if post_data:
            self.server.content = post_data

        self.send_response(200)
        self.end_headers()

class TestServer(HTTPServer):

    def __init__(self, serverPort: int) -> None:
        self.server_address = ('', serverPort)
        super().__init__(('', serverPort), SimpleHTTPRequestHandler)
        self.serverRunning = False
        self.server_thread = None
        self.content = b"<html><body><h1>My Website!</h1></body></html>"

    def startServer(self):
        if not self.serverRunning:
            print(f'Starting httpd on port {self.server_address[1]}...')
            self.server_thread = threading.Thread(target=self.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            self.serverRunning = True

    def stopServer(self):
        if self.serverRunning:
            print('Stopping httpd...')
            self.shutdown()
            self.server_close()
            self.serverRunning = False
            self.server_thread.join()

if __name__ == "__main__":
    server = TestServer(8000)
    server.startServer()
    while True: pass
