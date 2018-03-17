# -*- coding: utf-8 -*-
    
import os
    
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
    
from tornado.options import define, options
    
define("port", default=8888, help="run on the given port", type=int)
    
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", RootHandler),
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)
    
class RootHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    
    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
if __name__ == "__main__":
    main()