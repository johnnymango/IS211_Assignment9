#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assignment 9 - Scraping Stock Data"""

from bs4 import BeautifulSoup
import urllib2
import pandas as pd


#Functions scraps stock data.
def stock_scraper():
    url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')

    #This soup object allows access to the opening price.  Can't access closing price.
    table = soup.find_all('table')[0].find_all('tr', attrs={'class':'BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)'})


    #This soup oject allows for the closing price but only returns the first item.
    #table = soup.find_all("tbody")

    #Creates dictionary to hold the date and price values
    mydict ={}

    #Searches the soup object for the date and price and updates dictionary.
    for item in table:
        date = item.find_all('td')[0].find_all('span')[0].contents[0]
        price = item.find_all('td')[1].find_all('span')[0].contents[0]
        mydict[date] = price


    #Converts dict to dataframe for presentation.
    df1 = pd.DataFrame(mydict.items(), columns=['Date', 'Opening Price'])
    print df1

if __name__ == "__main__":
    stock_scraper()