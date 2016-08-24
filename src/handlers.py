from elasticsearch import Elasticsearch
import config
import tornado.web
import tornado.escape
import helpers
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class Suggest(tornado.web.RequestHandler):

    def post(self):

        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST")

        body = self.request.body
        if body:

            es = self.application.database
            suggestions = helpers.suggest(es, body)
            self.write(json.dumps({"suggestions":suggestions}))
        else:
            self.write("no suggesiton.")


    def options(self):

        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "OPTIONS")

        body = self.request.body
        if body:
            #suggestion = tornado.escape.json_decode(body)
            suggestions = helpers.suggest(body)
            self.write(json.dumps({"suggestions":suggestions}))
        else:
            self.write("no suggesiton.")
