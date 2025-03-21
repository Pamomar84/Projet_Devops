from http.server import HTTPServer, BaseHTTPRequestHandler  
class SimpleHandler(BaseHTTPRequestHandler):     
    def do_GET(self):
        self.send_response(200)  
        self.send_header("Content-type", "text/html")         
        self.end_headers()  
        with open("server.html", "rb") as file:  
                self.wfile.write(file.read())      
        #self.wfile.write(message.encode("utf-8"))  
if __name__ == "__main__":
    server_address = ("0.0.0.0", 8000)  
    httpd = HTTPServer(server_address, SimpleHandler)     
    print("Serving on port 8000...")     
    httpd.serve_forever()













"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):    
    def do_GET(self):
        self.send_response(200)
        
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        self.wfile.write(b"Hello, Docker World!")

def run(server_class=HTTPServer, handler_class=SimpleHandler):
            server_address = ('0.0.0.0', 8000)
    
            httpd = server_class(server_address, handler_class)
    
            print("Starting server on port 8000...")
    
            httpd.serve_forever()

if __name__ == "__main__":
    run()
"""