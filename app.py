# -*- coding: utf-8 -*-
"""
测试代码
"""
import os.path
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options

import controllers.apis
import controllers.gallery

define("port", default=8000, help="run on the given port", type=int)
define("debug", default=True, help="run on the given port", type=bool)


class Application(tornado.web.Application):
    """ 初始化应用 """

    def __init__(self):
        #
        handlers = [
            (r"/", MainHandler),
            (r"/api/([\w+\-]+)", controllers.apis.ApiHandler)
        ]

        handlers.extend(controllers.gallery.getHandlers())

        # 设置参数
        settings = dict(
            # 设置模板文件位置
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # 设置静态文件位置
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    """ 默认请求 """

    def get(self):

        self.render(
            "index.html",
            page_title="Burt's Books | Home",
            header_text="Welcome to Burt's Books!",
            footer_text="footer text")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
