# -*- coding: utf-8 -*-
"""
OAuth 2.0
"""

import uuid
import json

from sqlalchemy import select, text

import x.data.orm
from x.web.apis import WebApiResponse

from models.membership import Account, Member
from models.connect import ConnectAuthorizationCode, ConnectAccessToken


class Auth(object):
    """ 验证管理 """

    def authorize(self, req, res=WebApiResponse()):
        """
        授权验证
        :param clientId: 客户端应用
        :param redirectUri: 重定向地址
        :param responseType: 响应类型
        :param scope: 授权范围
        :param style: 样式 自定义样式
        :param loginName: 登录名
        :param password: 密码
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
        """
        clientId = req.get("clientId")
        redirectUri = req.get("redirectUri")
        responseType = req.get("responseType")
        scope = req.get("scope")
        style = req.get("style")
        loginName = req.get("loginName")
        password = req.get("password")

        session = x.data.orm.createSession()

        # 获取当前用户信息

        account = session.query(Account).filter(
            text("loginName='" + loginName + "' and password='" + password + "'")).first()

        if account is None:
            if responseType is None:
                res.message.returnCode = 1
                res.message.value = u"帐号或者密码错误。"
                return res
            else:
                # 如果响应类型
                # TODO: 输出登录页面
                pass
        else:
            # 检验是否有授权码
            # cliendId account
            authorizationCode = session.query(ConnectAuthorizationCode).filter(
                text("appKey='" + clientId + "' and accountId='" + account.id + "'")).first()

            # 如果不存在则新增授权码信息
            if authorizationCode is None:
                # 设置对象信息
                authorizationCode = ConnectAuthorizationCode()

                authorizationCode.id = str(uuid.uuid4())
                authorizationCode.appKey = clientId
                authorizationCode.accountId = account.id
                authorizationCode.authorizationScope = scope == '' and "public" or scope

                session.add(authorizationCode)
                # 写数据库，但并不提交
                session.flush()
                session.commit()

            # 设置访问令牌

            # 设置会话信息
            accessToken = session.query(ConnectAccessToken).filter(
                text("appKey='" + clientId + "' and accountId='" + account.id + "'")).first()

            # 如果不存在则新增授权码信息
            if accessToken is None:

                accessToken = ConnectAccessToken(id=str(uuid.uuid4()))

                # 设置对象信息
                accessToken.id = str(uuid.uuid4())
                accessToken.appKey = clientId
                accessToken.accountId = account.id
                accessToken.authorizationScope = scope == '' and "public" or scope

                session.add(accessToken)
                # 写数据库，但并不提交
                # session.flush()
                session.commit()

            # 记录日志
            res.data = accessToken
            res.message.returnCode = 0
            res.message.value = u"验证成功。"

            return res

        print "authorize loginName:" + loginName + " password:" + password

        res.message.returnCode = 0
        res.message.value = u"执行成功。"

        return res

    def token(self,  req, res=WebApiResponse()):
        """
        获取令牌信息
        :param code: 授权码信息
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
        """
        code = req.get("code")

        session = x.data.orm.createSession()

        authorizationCode = session.query(ConnectAuthorizationCode).filter_by(
            id=code).first()

        # 如果不存在则新增授权码信息
        if authorizationCode is None:
            res.message.returnCode = 1
            res.message.value = "authorization code not find"
            return res

        accessToken = session.query(ConnectAccessToken).filter(
            text("appKey='" + authorizationCode.appKey + "' and accountId='" + authorizationCode.accountId + "'")).first()

        if accessToken is None:
            res.message.returnCode = 1
            res.message.value = "access code not find"
            return res

        return res

    def refresh(self, req, res=WebApiResponse()):
        """ 刷新令牌信息 """
        print "token"
        return "connect.auth.refresh"

    def me(self, req, res=WebApiResponse()):
        """ 当前用户信息 """
        token = req.get("token")

        session = x.data.orm.createSession()

        accessToken = session.query(
            ConnectAccessToken).filter_by(id=token).first()

        if accessToken is None:

            res.message.returnCode = 1
            res.message.value = "people not find"
            return res
        else:
            # 根据访问令牌返回当前湖用户
            # IMemberInfo member =
            # MembershipManagement.Instance.MemberService[accessTokenInfo.AccountId]
            member = session.query(Member).filter_by(
                id=accessToken.accountId).first()

            if member is None:

                res.message.returnCode = 1
                res.message.value = "people not find"
                return res

            # 输出个人信息
            res.data = member

            res.message.returnCode = 0
            res.message.value = "success"

            return res

    def ToPeopleJson(self, account):
        """ 将人员信息格式化为特定格式 """
        return {
            "id": account.id,
            "name": account.name,
            "loginName": account.loginName,
            # "certifiedAvatar": account.certifiedAvatar,
            "status": account.status
        }
