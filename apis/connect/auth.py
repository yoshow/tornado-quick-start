# -*- coding: utf-8 -*-
"""

"""


class Auth:
    """ 验证管理 """

    def authorize(self):
        """ 验证管理 """
        print "authorize"
        return "connect.auth.authorize"

    def token(self):
        """ 获取令牌信息 """
        print "token"
        return "connect.auth.token"
