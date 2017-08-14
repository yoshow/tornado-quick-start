# -*- coding: utf-8 -*-
"""
Web API 管理
"""

import logging
import json
import datetime


def invoke(methodName, req):
    """ 执行动态方法 """
    methodName = methodName.replace('/', '.')
    keys = methodName.split('.')

    if len(keys) < 2:
        raise Exception("method name error.")

    # 映射对应的方法名和类名
    methodName = keys.pop()
    modulePath = '.'.join(keys)
    moduleName = keys.pop()
    className = moduleName.capitalize()

    # 支持模块和类名名称一样的简写
    if modulePath.find('.') == -1:
        modulePath = '.'.join([modulePath, modulePath])

    # 记录参数信息
    logging.info('moduleName:' + moduleName + ' className:' +
                 className + ' methodName:' + methodName)

    # 导入模块
    target = __import__(modulePath)
    target = getattr(target, moduleName)
    # 获取对象信息
    Object = getattr(target, className)
    # 初始化类
    target = Object()
    # 获取方法信息
    method = getattr(target, methodName)

    res = createResponse()

    # 执行方法
    return method(req, res)


def verify(token, level):
    """
    验证安全性
    token 访问令牌
    level 验证的级别
    """
    return 0


def createResponse():
    """
    创建响应信息
    """
    response = WebApiResponse()

    return response


class WebApiResponse:
    """
    Web API 响应信息
    """

    def __init__(self):
        self.data = ''
        # value 返回的值
        # message = null
        self.message = WebApiMessage()
        # pass

    def json(self):
        """
        转为 JSON 字符串
        """
        _data = self.data
        if isinstance(self.data, list):
            _data = object_to_dict(_data)
        elif isinstance(self.data, object):
            _data = object_to_dict(_data)
        else:
            pass

        result = {
            "data": _data,
            "message": object_to_dict(self.message)
        }

        return json.dumps(result)


class WebApiMessage:
    """
    Web API 响应信息
    """
    returnCode = "0"
    # 返回的值
    value = ""


def object_to_dict(obj):
    """
    summary:
        将object转换成dict类型
    """
    _dict = {}

    members = [m for m in dir(obj)]

    for m in members:
        if m[0] != "_" and not callable(m):
            value = getattr(obj, m)

            # 字符串类型
            if isinstance(value, str):
                _dict[m] = value
            # 数字类型
            elif isinstance(value, int) or isinstance(value, float):
                _dict[m] = value
            # datetime 类型转为字符串类型
            elif isinstance(value, datetime.datetime):
                _dict[m] = value.strftime('%Y-%m-%d %H:%M:%S')
            else:
                pass

    return _dict
