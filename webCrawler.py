# @Author: jiGg4
# @Date:   28-02-2017
# @Email:  jigg4@me.com
# @Filename: webCrawler.py
# @Last modified by:   jiGg4
# @Last modified time: 01-03-2017



#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request, parse
import re, sys

url = "https:" + parse.quote("//de.wikipedia.org/wiki/Liste_von_Nestlé-Marken")

site = request.urlopen(url)

html = site.read().decode()

regO = re.findall("http[a]*:\/\/\w*\.\w{1,3}\/*\w*\W\w*\W\w*\W\w*\W\w*\W\w*\W", html)

print(regO)
#for i in regO:
#    print(i,"\n")
