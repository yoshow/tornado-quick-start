# -*- coding: utf-8 -*-
"""

"""
import json

import tornado.web
import x.web.apis


class ApiHandler(tornado.web.RequestHandler):
    """ API 请求函数 """

    def get(self, menthodName):
        """ API """
        # 设置参数
        args = {}
        keys = self.request.arguments.keys()
        for name in keys:
            args[name] = self.get_argument(name)

        output = x.web.apis.invoke(menthodName, args)
        self.write(output)

    def post(self, menthodName):
        """ POST """
        # 设置参数
        args = {}

        # 处理 JSON 格式请求
        if self.request.headers['Content-Type'] == 'application/json':
            args = json.loads(self.request.body)
        else:
            keys = self.request.arguments.keys()
            for name in keys:
                args[name] = self.get_argument(name)

        output = x.web.apis.invoke(menthodName, args)
        self.write(output)

if __name__ == '__main__':
    # auth
    # http://localhost:8000/api/connect/auth/authorize

    x.web.apis.invoke('connect/auth/authorize')
    x.web.apis.invoke('api_test.mod1')

    x.web.apis.invoke('auth.mod1')
