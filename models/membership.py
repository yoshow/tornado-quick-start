# -*- coding: utf-8 -*-
"""
帐号信息
"""

from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    """ 帐号信息 """

    __tablename__ = 'tb_Account'
    id = Column(String(36), primary_key=True)
    code = Column(String(30))
    name = Column(String(50))
    loginName = Column(String(50))
    password = Column(String(50))
    status = Column(Integer())
    createdDate = Column(DateTime())


class Member(Base):
    """ 成员信息 """

    __tablename__ = 'tb_Member'
    id = Column(String(36), primary_key=True)
    accountId = Column(String(36))

    createdDate = Column(DateTime())


class Role(Base):
    """ 角色信息 """

    __tablename__ = 'tb_Role'
    id = Column(String(36), primary_key=True)
    code = Column(String(30))
    name = Column(String(50))
    status = Column(Integer())
    createdDate = Column(DateTime())
