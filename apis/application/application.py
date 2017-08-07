# -*- coding: utf-8 -*-
"""
Application
"""


class Application(object):
    """ 应用管理 """

    def __init__(self):
        pass

    def query(self, args):
        """ 分页查询信息 """
        print "query"
        return 'application.query()'

    def findOne(self, args):
        """ 查询某条记录 """

        if "id" not in args.keys():
            return u'参数错误'

        return 'application.findOne("' + args["id"] + '")'

    def create(self):
        """ 获取令牌信息 """
        print "token"
        return 'query.create'

    def delete(self):
        """ 获取令牌信息 """
        print "token"
        return 'connect.auth.token'
