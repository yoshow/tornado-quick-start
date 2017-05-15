# -*- coding: utf-8 -*-
"""

"""

import sys
sys.path.append("..")

from models.membership import Account

from sqlalchemy import create_engine, MetaData,\
    Table, Column, Integer, String, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import datetime
import time
import mysql.connector

import tornado.web


def getHandlers():
    """ """

    prefixUrl = r"/account/"

    handlers = [
        (prefixUrl + "sign-in", SignInHandler),
        (prefixUrl + "sign-out", SignOutHandler),
        # (r"/gallery/detail", DetailHandler),
    ]

    return handlers


class SignUpHandler(tornado.web.RequestHandler):
    """ """

    def get(self):
        self.render(
            "index.html",
            page_title="List | Gallery",
            header_text="form",
            footer_text="footer text"
        )


class SignInHandler(tornado.web.RequestHandler):
    """ """

    def get(self):
        self.render(
            "index.html",
            page_title="List | Gallery",
            header_text="form",
            footer_text="footer text"
        )


class SignOutHandler(tornado.web.RequestHandler):
    """ """

    def get(self):

        engine = create_engine(
            'mysql+mysqlconnector://test:test@localhost/CW_BigDb', echo=True)

        metadata = MetaData(engine)

        # user_table = Table(
        #     'tb_Account', metadata,
        #     Column('id', Integer, primary_key=True),
        #     Column('name', String(50)),
        #     Column('fullname', String(100))
        # )

        user_table = Table('tb_Account', metadata, autoload=True)

        print 'user' in metadata.tables
        print [c.name for c in user_table.columns]

        Session = sessionmaker(bind=engine)
        session = Session()

        # first()第一个 all()全部
        result = session.query(Account).filter_by(
            id='00000000-0000-0000-0000-000000000001').first()

        print result.name
        print result.createdDate.strftime("%Y-%m-%d %X")

        self.render(
            "gallery/detail.html",
            title="Detail | Gallery",
            header="Detail",
            content=result.name + '<br>' +
            result.createdDate.strftime("%Y-%m-%d %X"),
            result=result,
            footer="footer text"
        )
