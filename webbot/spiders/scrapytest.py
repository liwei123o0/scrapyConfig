# -*- coding: utf-8 -*-
#! /usr/bin/env python

import sys
from webbot.zujian import confload
from scrapy.spiders import CrawlSpider

class ScrapyCrawl(CrawlSpider):

    name = 'spider'
    #实例化ConfigProject类
    config = confload.ConfigProject()
    #加载配置文件
    txt = config.loadconfig(sys.argv[3].replace("path=",""))


