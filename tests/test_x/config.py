# -*- coding: utf-8 -*-
"""
test x
"""
import unittest
import x.config


class TestConfig(unittest.TestCase):

    # 初始化工作
    def setUp(self):
        # 实例化了被测试模块中的类
        self.target = x.config.init('app.yaml')

    # 退出清理工作
    def tearDown(self):
        self.target = None

    # 具体的测试用例，一定要以test开头
    def test_init(self):
        # self.assertEqual(self.config.sum(1, 2), 3)
        config = x.config.init('app.yaml')
        assert config is not None
        assert config.http_server.debug is True

if __name__ == '__main__':
    unittest.main()
