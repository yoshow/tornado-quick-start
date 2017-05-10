# -*- coding: utf-8 -*-
"""
帐号信息
"""

from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = 'tb_Account'
    id = Column(String(36), primary_key=True)
    code = Column(String(30))
    name = Column(String(50))
    loginName = Column(String(50))
    status = Column(Integer())
    createdDate = Column(DateTime())
