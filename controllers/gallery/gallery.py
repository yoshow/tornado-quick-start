# -*- coding: utf-8 -*-
"""

"""

import uuid
import datetime
import time

from models.gallery import Gallery
from models.membership import Account

import mysql.connector

import tornado.web

import x.data.orm


def getHandlers():
    """ 配置路由处理规则 """

    handlers = [
        (r"/gallery/list", ListHandler),
        (r"/gallery/form", FormHandler),
        (r"/gallery/form/([\w+\-]+)", FormHandler),
        (r"/gallery/detail/([\w+\-]+)", DetailHandler),
    ]

    return handlers


class FormHandler(tornado.web.RequestHandler):
    """ 表单处理 """

    def get(self, id=''):
        print 'id:' + id

        param = Gallery(
            id=id,
            name='',
            code='')

        if id == '':
            self.render(
                "gallery/gallery-form.html",
                title="Form | Gallery",
                header="form",
                footer="footer text",
                param=param
            )
        else:
            session = x.data.orm.createSession()

            param = session.query(Gallery).filter_by(id=id).first()
            self.render(
                "gallery/gallery-form.html",
                title="Form | Gallery",
                header="form",
                param=param
            )

    def post(self):
        """ """

        identity = self.get_argument('id')
        code = self.get_argument('code')
        name = self.get_argument('name')

        param = None

        session = x.data.orm.createSession()

        if session.query(Gallery).filter(Gallery.id == identity).count() == 0:
            param = Gallery(id=str(uuid.uuid4()))
            # 添加到数据库
            session.add(param)
            # 写数据库，但并不提交
            session.flush()
        else:
            param = session.query(Gallery).filter(Gallery.id == identity).one()

        # 设置对象信息
        param.code = code
        param.name = name
        param.modifiedDate = datetime.datetime.now()

        session.add(param)
        session.commit()

        self.write('提交成功!<br/>')
        self.write(name + "<br />")
        self.write('<a href="list">返回列表</a>')
        # self.redirect('list')


class DetailHandler(tornado.web.RequestHandler):
    """ 明细处理 """

    def get(self, id):
        session = x.data.orm.createSession()

        # first()第一个 all()全部
        result = session.query(Gallery).filter_by(id=id).first()

        self.render(
            "gallery/gallery-detail.html",
            title="Detail | Gallery",
            header="Detail",
            content=result.name + '<br>' +
            result.createdDate.strftime("%Y-%m-%d %X"),
            result=result,
            footer="footer text"
        )


class ListHandler(tornado.web.RequestHandler):
    """ 列表 """

    def get(self):

        outString = ''

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='cw_bigdb')

        cursor = cnx.cursor()

        query = ("SELECT Name, CreatedDate FROM tb_Account "
                 "WHERE CreatedDate BETWEEN %s AND %s")

        hire_start = datetime.date(1970, 1, 1)
        hire_end = datetime.date(1999, 12, 31)

        cursor.execute(query, (hire_start, hire_end))

        for (Name, CreatedDate) in cursor:
            outString += Name + "<br>"
            # print Name
            # print CreatedDate
            # print "{} was hired on {:%d %b %Y}".format(Name, CreatedDate)

        cursor.close()
        cnx.close()

        session = x.data.orm.createSession()

        # first()第一个 all()全部
        result = session.query(Gallery)

        self.render(
            "gallery/gallery-list.html",
            title="List | Gallery",
            header='',
            list=result,
            footer="footer text"
        )
