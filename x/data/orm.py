# -*- coding: utf-8 -*-
"""
数据库管理
"""

from sqlalchemy import create_engine, MetaData,\
    Table, Column, Integer, String, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import x.config


def createEngine():
    """ 创建引擎 """

    # 配置信息
    config = x.config.init('app.yaml')

    connectionString = config.database.provider + '+mysqlconnector://' + \
        config.database.loginName + ':' + config.database.password + \
        '@' + config.database.datasource + '/' + config.database.database

    engine = create_engine(connectionString, echo=True)
    return engine


def createSession(engine=None):
    """ 创建会话 """
    if engine is None:
        engine = createEngine()

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
