#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import pandas as pd

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")

table = soup.findAll("table", attrs={"class":"data"})[0].findAll('tr', attrs={"valign":"top"})

list = []
for i in table:
    name = (i.findAll('td')[0].findAll('a')[0].contents[0])
    list.append(name)

print list

df1 = pd.DataFrame(list)

print df1