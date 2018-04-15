# -*- coding: utf-8 -*-
    
import os
    
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.escape

from tornado.web import RequestHandler
from tornado.options import define, options
    
define("port", default=80, help="run on the given port", type=int)
    
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", RootHandler),
            (r"/observer", ObserverHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)
    
class RootHandler(RequestHandler):
    def get(self):  
        #self.write("Aloha!")
        self.render('start.html')

class ObserverHandler(RequestHandler):
    def get(self):
        self.write("Observer")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        args = str(self.request.arguments)
        self.write("You wrote " + args)
        #self.write("You wrote " + self.get_body_argument("message"))

    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
if __name__ == "__main__":
    main()