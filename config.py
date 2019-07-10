# -*- coding: utf-8 -*-
import os

from utils import YAMLBase


class ConfigParser(YAMLBase):
    def __init__(self, filepath=None):
        if not filepath: filepath = 'config.yml'
        super(ConfigParser, self).__init__(filepath)

