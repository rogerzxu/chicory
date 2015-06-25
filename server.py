__author__ = 'Roger'

import SimpleHTTPServer
import SocketServer
import minesweeper
from urlparse import parse_qs

PORT = 8000

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['content-length'])
        postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
        if postvars['turn']:
            self.game
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.game = minesweeper.Minesweeper(int(postvars['height'][0]), int(postvars['width'][0]), int(postvars['mines'][0]))
            with open ("templates/minesweeper.html", "r") as myfile:
                data=myfile.read()
            html = data.format(grid=self.game)
            self.wfile.write(html)

Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()