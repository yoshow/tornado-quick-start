# coding=utf-8
import unittest
# import HTMLTestRunner

import tests.test_x.config
import tests.test_x.web.apis
import tests.test_apis.connect.auth

if __name__ == "__main__":
    # 注意使用套件时，在单个py文件中下的多个用例用  (类名（"方法名")),
    # 导入多个py的类下，用（py名.类名）

    suite = unittest.TestSuite()
    # 测试 支持类
    suite.addTest(unittest.makeSuite(tests.test_x.config.TestConfig))
    suite.addTest(unittest.makeSuite(tests.test_x.web.apis.TestApis))
    # 测试 API接口类
    suite.addTest(unittest.makeSuite(tests.test_apis.connect.auth.TestAuth))
    # suite.addTest(unittest.makeSuite(product.test_product))
    runner = unittest.TextTestRunner()

    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # filename = 'C:\\Users\\DELL\\Desktop\\Report\\' + now + "test_all.html"
    # fp = file(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #    stream=fp, title=u'产品管理和分类管理的自动化测试报告', description=u'测试用例结果')
    # runner.run(suite)
    # fp.close()

    runner.run(suite)
