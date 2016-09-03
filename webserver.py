#!/usr/bin/python

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.htm")
        print 'received a request'


class UploadHandler(tornado.web.RequestHandler):             # +
    def post(self):                                          # +
        file_contents = self.request.files['file'][0].body   # +
        file_ori_name = self.request.files['file'][0].filename

        print 'get', file_ori_name

        with open(u"uploads/"+file_ori_name, "wb") as f:     # +
            f.write(file_contents)                           # +
        self.finish()                                        # +


application = tornado.web.Application([
    (r"/file-upload", UploadHandler),                        # +
    (r"/", MainHandler),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
])

if __name__ == "__main__":
    application.listen(8964)
    tornado.ioloop.IOLoop.instance().start()
