# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class SwaggerOperation(object):
    def __init__(self, **kwargs):
        self.data = kwargs

    def render(self):
        return self.data
