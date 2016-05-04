# -*- coding: utf-8 -*-
#! /usr/bin/env python

import urllib2
import json
import logging

class ConfigProject(object):
    #读取配置文件
    def loadconfig(self,path):
        try:
            txt = urllib2.urlopen("file:\\\%s"%path).read()
        except:
            raise logging.error(u"检查配置文件路径是否正确!")
        return json.loads(txt)

if __name__ =='__main__':

    pass