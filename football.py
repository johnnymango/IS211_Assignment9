#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import pandas as pd

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")

table = soup.findAll("tr")

print table