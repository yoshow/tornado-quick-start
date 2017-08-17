#!/usr/bin/env python
# coding: utf-8
"""
test coonect auth
"""
import unittest

import x.web.apis
import apis.connect.auth


class TestAuth(unittest.TestCase):
    """ Connect 应用 Auth 接口 """

    def setUp(self):
        # 初始化工作
        # 实例化了被测试模块中的类
        self.target = apis.connect.auth.Auth()

    # 退出清理工作
    def tearDown(self):
        self.target = None

    def test_authorize(self):
        """ 测试授权验证接口 """

        # 正常的请求
        req = {
            "clientId": "9b722c14-9e93-46aa-a4fc-ad2b2f790c19",
            "loginName": "admin",
            "password": "96eae1e4c7b84a62be740d209e5ca61e4b76b40f"
        }

        res = self.target.authorize(req)

        assert res is not None
        assert res.message.returnCode == 0
        assert res.data is not None

        # 异常请求 - 密码错误
        req = {
            "clientId": "9b722c14-9e93-46aa-a4fc-ad2b2f790c19",
            "loginName": "admin",
            "password": "96eae1e4c7b84a62"
        }

        res = self.target.authorize(req)

        assert res is not None
        assert res.message.returnCode == 1
        assert res.data is not None

    def test_token(self):
        """ 测试获取访问令牌接口 """

        req = {
            "code": "2105b087e39340e5975d9a6f76e8bfc8"
        }

        res = self.target.token(req, x.web.apis.createResponse())

        assert res is not None
        # assert res.message.returnCode == 0

    def test_me(self):
        """ 测试获取当前用户信息接口 """

        req = {
            "token": "e9fbd878ec784369afd3e995fb1f53cc"
        }

        res = self.target.me(req, x.web.apis.createResponse())

        assert res is not None
        assert res.message.returnCode is not None
        assert res.data is not None

        req = {"token": ""}

        res = self.target.me(req)

        assert res is not None
        assert res.message.returnCode == 1
        assert res.data == ''

if __name__ == '__main__':
    unittest.main()
