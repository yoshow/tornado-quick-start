# coding: utf-8
"""

"""

import unittest
import tests.test_x.config

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tests.test_x.config.TestConfig))
    # suite.addTest(MyTestCase("testCase2"))

    # 确定生成报告的路径
    # 生成报告的Title,描述
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
