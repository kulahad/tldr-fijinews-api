from bs4 import BeautifulSoup as bs
import requests as req
import sqlite3
import datetime as dt

class newsItem(object):
    Id = 0
    header = ''
    link = ''
    time = ''

    def __init__(self, newsId, header, link, time):
        self.Id = newsId
        self.header = header
        self.link = link
        self.time = time


def store_data_to_db(newsList):
    conn = sqlite3.connect('News.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS NEWS
           (ID INT PRIMARY KEY     NOT NULL,
           HEADER           TEXT     NULL,
           LINK            BLOB      NULL,
           TIME            TEXT      NULL);''')
    print("Table created successfully")

    for item in newsList:
        query = f'INSERT OR IGNORE INTO NEWS (ID,HEADER,LINK,TIME) \
            VALUES \
          ({item.Id}, "{item.header}", "{item.link}","{item.time}");'
        conn.execute(query)

    conn.commit()
    print("Records created successfully")
    conn.close()


fijivillage = req.get("https://fijivillage.com")
isAvailable = fijivillage.status_code
html = fijivillage.text
newsList = []

if isAvailable == 200:
    parsed_html = bs(html, "html.parser")
    alldiv = parsed_html.find_all('div')

    for div in alldiv:
        if div.h6:
            if div.find('span'):
                newsAge = div.find('span').text
                timeNow = dt.datetime.now()
                if newsAge[2] == "h":
                    time = timeNow - dt.timedelta(hours=int(newsAge[0]))
                elif newsAge[2] == "d":
                    time = timeNow - dt.timedelta(days=int(newsAge[0]))
            story = newsItem(id(div.h6.string), div.h6.string, div.a['href'], time)
            newsList.append(story)
        elif div.h3:
            if div.find('span'):
                newsAge = div.find('span').text
                timeNow = dt.datetime.now()
                if newsAge[2] == "h":
                    time = timeNow - dt.timedelta(hours=int(newsAge[0]))
                elif newsAge[2] == "d":
                    time = timeNow - dt.timedelta(days=int(newsAge[0]))
            story = newsItem(id(div.h3.string), div.h3.string, div.a['href'], time)
            newsList.append(story)

store_data_to_db(newsList)
