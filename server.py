__author__ = 'Roger'

import SimpleHTTPServer
import SocketServer
import minesweeper
from urlparse import parse_qs

PORT = 8000

game = None

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['content-length'])
        postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
        global game
        if 'turn' in postvars:
            row = int(postvars['turn'][0][0])
            column = int(postvars['turn'][0][1])
            game.turn(row, column)
            with open ("templates/minesweeper.html", "r") as myfile:
                data=myfile.read()
            html = data.format(grid=game)
            self.wfile.write(html)
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            game = minesweeper.Minesweeper(int(postvars['height'][0]), int(postvars['width'][0]), int(postvars['mines'][0]))
            with open ("templates/minesweeper.html", "r") as myfile:
                data=myfile.read()
            html = data.format(grid=game)
            self.wfile.write(html)

Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()