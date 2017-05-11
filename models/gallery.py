# -*- coding: utf-8 -*-
"""
图库管理
"""
import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gallery(Base):
    """ 图库信息 """
    __tablename__ = 'tb_Gallery'
    id = Column(String(36), primary_key=True)
    code = Column(String(30))
    name = Column(String(50))
    status = Column(Integer)
    modifiedDate = Column(DateTime, default=datetime.datetime.utcnow)
    createdDate = Column(DateTime, default=datetime.datetime.utcnow)
