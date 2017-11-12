#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assignment 9 - Scraping CBS Sports for Touchdown Data"""

from bs4 import BeautifulSoup
import urllib2
import pandas as pd

#Function creates the soup object, parses the data and passes to a pandas data frame for presentation.
def td_scraper():

        #Loads the URL and create the soup object
        url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, "lxml")
        table = soup.find_all("table", attrs={"class":"data"})[0].find_all('tr', attrs={"valign":"top"})

        #Creates lists to save the data that will be parsed from the soup object
        name_list = []
        td_list = []
        position_list = []
        team_list = []

        #Loop parses the data and updates the list.
        for i in table:
            name = i.find_all('td')[0].find_all('a')[0].contents[0]
            name_list.append(name)

            tds = i.find_all('td')[6].contents[0]
            td_list.append(tds)

            pos = i.find_all('td')[1].contents[0]
            position_list.append(pos)

            team = i.find_all('td')[2].find_all('a')[0].contents[0]
            team_list.append(team)

        #Creates a dataframe from the lists and presents the top 20 players
        df1 = pd.DataFrame(dict(Player=name_list, Team=team_list, TouchDowns=td_list, Position=position_list ))
        print df1.head(20)

if __name__ == "__main__":
    td_scraper()