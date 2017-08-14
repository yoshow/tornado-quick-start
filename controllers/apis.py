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
        req = {}
        keys = self.request.arguments.keys()

        if len(keys) == 0:
            self.write('request arguments is empty.')
            return

        for name in keys:
            req[name] = self.get_argument(name)

        output = x.web.apis.invoke(menthodName, req)
        self.write(output)

    def post(self, menthodName):
        """ POST """
        # 设置参数
        req = {}

        # 处理 JSON 格式请求
        if self.request.headers['Content-Type'] == 'application/json':
            req = json.loads(self.request.body)
        else:
            keys = self.request.arguments.keys()
            for name in keys:
                req[name] = self.get_argument(name)

        res = x.web.apis.invoke(menthodName, req)
        if isinstance(res, str):
            self.write(res)
        if isinstance(res, str):
            self.write(res.json())
        else:
            self.write(res)
    # auth
    # http://localhost:8000/api/connect/auth/authorize

    x.web.apis.invoke('connect/auth/authorize')
    x.web.apis.invoke('api_test.mod1')

    x.web.apis.invoke('auth.mod1')
