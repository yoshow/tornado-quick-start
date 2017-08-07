# -*- coding: utf-8 -*-
"""
OAuth 2.0
"""


class Auth:
    """ 验证管理 """

    def authorize(self, args):
        """ 验证管理 """
        print "authorize"
        return "connect.auth.authorize"

    def token(self, args):
        """ 获取令牌信息 """
        print "token"
        return "connect.auth.token"
