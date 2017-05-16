# -*- coding: utf-8 -*-
"""
Web API 管理
"""

import logging

import x.config


def invoke(methodName, args):
    """ 执行动态方法 """
    methodName = methodName.replace('/', '.')
    keys = methodName.split('.')
    # 映射对应的方法名和类名
    methodName = keys.pop()
    modulePath = '.'.join(keys)
    moduleName = keys.pop()
    className = moduleName.capitalize()

    # 支持模块和类名名称一样的简写
    if modulePath.find('.') == -1:
        modulePath = '.'.join([modulePath, modulePath])

    # 记录参数信息
    logging.info('moduleName:' + moduleName + 'className:' +
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
    # 执行方法
    return method(args)
