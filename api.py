import tornado.ioloop
import tornado.web
from customers import Customers
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

customers = Customers()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Customers Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addcust", AddHandler, dict(customers = customers)),
        (r"/v1/delcust", DelHandler, dict(customers = customers)),
        (r"/v1/getcust", GetHandler, dict(customers = customers)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
