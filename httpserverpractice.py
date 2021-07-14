import http.server

# Create the handler class to respond to requests
class Handler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    # 200 is the http status code for "OK"--request succeeded:
    self.send_response(200)
    # Our handler will respond to a request in plain text:
    self.send_header('Content-Type', 'text/plain')
    self.end_headers ()
    # Write a file with that says 'Hello!' in response to a request:
    self.wfile.write('Hello!\n'.encode())

if __name__ == '__main__':
  server = ('', 8118)   # (host, port_number)
  print(f"Serving at {server} \n")
  # Instantiate the Handler class:
  httpd = http.server.HTTPServer(server, Handler)
  # Activate the server and serve continuously:
  httpd.serve_forever()
  
  # Alternatively, we can just handle a single request as described in the lecture notes:
  # httpd.handle_request()
  # httpd.server_close()
