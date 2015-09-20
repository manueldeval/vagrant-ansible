from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import json
import socket
import sys

port = int(sys.argv[1])
me = {"hostname": socket.gethostname()}

class MyRequestHandler (BaseHTTPRequestHandler) :

    def do_GET(self) :
		#send response code:
        self.send_response(200)
        #send headers:
        self.send_header("Content-type:", "application/json")
        # send a blank line to end headers:
        self.wfile.write("\n")
		#send response:
        json.dump(me, self.wfile)

server = HTTPServer(("0.0.0.0", port), MyRequestHandler)

server.serve_forever()

