from elasticsearch import Elasticsearch
import tornado.ioloop
import tornado.autoreload
import tornado.httpserver
import handlers
import config


class Application(tornado.web.Application):
    def __init__(self):

        _handlers = [
            (r"/", handlers.MainHandler),
            (r"/api/suggest", handlers.Suggest)
        ]

        tornado.web.Application.__init__(self, _handlers)

        self.database = Elasticsearch([{'host': str(config.HOST),
                                        'port': str(config.PORT)}])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()
