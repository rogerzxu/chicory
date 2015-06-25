__author__ = 'Roger'

import SimpleHTTPServer
import SocketServer
import minesweeper
from cgi import parse_header, parse_multipart
from urlparse import parse_qs

PORT = 8000

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(
                    self.rfile.read(length),
                    keep_blank_values=1)
        else:
            postvars = {}
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open ("templates/minesweeper.html", "r") as myfile:
            data=myfile.read()
        html = data.format(height=postvars['height'][0],width=postvars['width'][0],mines=postvars['mines'][0])
        self.wfile.write(html)

Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()