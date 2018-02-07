# -*- coding: utf-8 -*-
"""
cfg
"""
import json
import yaml


def init(file, file_type="yaml"):
    """ 初始化配置信息 """
    if file_type == "json":
        obj = json.load(open(file))
    elif file_type == "yaml":
        obj = yaml.load(open(file))

    return Configuration(obj)


class Configuration(object):
    """ 配置对象 """

    def __init__(self, map):
        self._map = map

    def __setattr__(self, name, value):
        if name == '_map':
            object.__setattr__(self, name, value)
            return
        print('set attr called ', name, value)
        self._map[name] = value

    def __getattr__(self, name):
        value = self._map[name]
        if isinstance(value, (dict)):
            return Configuration(value)
        if isinstance(value, (list)):
            r = []
            for i in value:
                r.append(Configuration(i))
            return r
        else:
            return self._map[name]

    def __getitem__(self, name):
        return self._map[name]
