# -*- coding: utf-8 -*-
"""
Account
"""

import x.data.orm
from x.web.apis import WebApiResponse

from models.membership import AccountInfo


class Account(object):
    """ 帐号管理 """

    def __init__(self):
        pass

    def findOne(self, req, res=WebApiResponse()):
        """ 查询某条记录 """
        idValue = req.get("id")

        session = x.data.orm.createSession()

        param = session.query(AccountInfo).filter(
            id=idValue).first()

        return 'application.findOne("' + args["id"] + '")'

    def query(self, req, res=WebApiResponse()):
        """ 查询某条记录 """

        return 'application.findOne("' + req.get("id") + '")'

    def create(self):
        """ 获取令牌信息 """
        print "token"
        return 'query.create'

    def delete(self):
        """ 获取令牌信息 """
        print "token"
        return 'connect.auth.token'

    def changePassword(self, req):
        """ 修改帐号密码 """
        print "query"
        return 'application.query()'
