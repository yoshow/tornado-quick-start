# -*- coding: utf-8 -*-
"""
测试代码
"""

import logging
import os.path
import sys

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options

import x.config

import controllers.apis
import controllers.account.account
import controllers.gallery.gallery

# 配置信息
config = x.config.init('app.yaml')


class Application(tornado.web.Application):
    """ 初始化应用 """

    def __init__(self):

        # 导入 Web API 服务
        sys.path.append(config.web.apis.path)

        # 配置默认路由
        handlers = [
            (r"/", MainHandler),
            (r"/api/([\w+\-\/]+)", controllers.apis.ApiHandler)
        ]

        # 配置路由 /gallery/
        handlers.extend(controllers.account.account.getHandlers())
        # 配置路由 /gallery/
        handlers.extend(controllers.gallery.gallery.getHandlers())

        # 设置参数
        settings = dict(
            # 设置模板文件位置
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # 设置静态文件位置
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=config.http_server.debug,
        )

        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    """ 默认请求 """

    def get(self):

        self.render(
            "index.html",
            title="Home",
            header_text="Welcome",
            footer_text="")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(config.http_server.port)
    # 启动时记录日志
    logging.info("Application Start")
    print "http://localhost:" + str(config.http_server.port)
    tornado.ioloop.IOLoop.instance().start()
    # 关闭时记录日志
    logging.info("Application Stop")
