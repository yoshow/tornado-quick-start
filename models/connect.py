# -*- coding: utf-8 -*-
"""
连接信息
"""

from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Connect(Base):
    """ 连接器信息 """

    __tablename__ = 'tb_Connect'
    id = Column(String(36), primary_key=True)
    appKey = Column(String(50))
    appSecret = Column(String(50))
    appType = Column(String(50))
    code = Column(String(30))
    name = Column(String(50))
    description = Column(String(50))
    status = Column(Integer())
    modifiedDate = Column(DateTime())
    createdDate = Column(DateTime())


class ConnectAuthorizationCode(Base):
    """ 连接器的授权代码信息 """

    __tablename__ = 'tb_Connect_AuthorizationCode'
    id = Column(String(36), primary_key=True)
    appKey = Column(String(36))
    accountId = Column(String(36))
    authorizationScope = Column(String(400))
    modifiedDate = Column(DateTime())
    createdDate = Column(DateTime())


class ConnectAccessToken(Base):
    """ 连接器的访问令牌信息 """

    __tablename__ = 'tb_Connect_AccessToken'
    id = Column(String(36), primary_key=True)
    appKey = Column(String(36))
    accountId = Column(String(36))
    expireDate = Column(DateTime())
    refreshToken = Column(String(36))
    modifiedDate = Column(DateTime())
    createdDate = Column(DateTime())
