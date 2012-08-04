from optparse import OptionParser
import os

import SimpleHTTPServer
import SocketServer

parser = OptionParser()
parser.set_description("Starts an HTTP server to enable transferring "
                       "files from one host to another.")
parser.add_option("-d", "--directory", dest="dirname", metavar="DIR",
                  help="The root directory for the server")
parser.add_option("-p", "--port", dest="port", metavar="PORT",
                  help="TCP port to listen on", type="int")

(options, args) = parser.parse_args()

port = options.port or 8000
dirname = options.dirname or ""
print port
print dirname

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", port), Handler)

print "serving at port", port
print "Use [Ctrl]+[C] to stop."
httpd.serve_forever()
