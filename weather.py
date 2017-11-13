#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assignment 9 - Scraping Weather Data"""

from bs4 import BeautifulSoup
import urllib2
import pandas as pd


#Creates the soup object and finds the temperature data.
url = 'https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'lxml')
table = soup.find_all('table', id='obsTable')[0].find_all('tbody')[0].find_all('td')
trs = soup.find_all('table', id='obsTable')[0].find_all('tr')[2:]
temperatures = [[td.getText() for td in trs[i].find_all('td')] for i in range(len(trs))]



#Creates the dataframe and performs positional selection of columns
df = pd.DataFrame(temperatures, index=None, dtype=int)
df2 = df.iloc[:,[0,2,3,4]]
df2.columns = ['Jan Date', 'High', 'Avg', "Low"]


#Function slices the dataframe to present the actual temps for the first 11 days of January.
def actual_temps():
    print "These are the Actual Temperatures Through Jan 11, 2015"
    print df2.head(11).to_string(index=False)
    print " "

#Function slices the datafram to present the forecast temp for the remaining 20 days in January.
def forecast_temps():
    print "These are the Forecast Temperature After Jan 11, 2015"
    print df2.tail(20).to_string(index=False)
    print " "

if __name__ == "__main__":
    actual_temps()
    forecast_temps()