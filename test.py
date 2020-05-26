from bs4 import BeautifulSoup as bs
import requests as req
import sqlite3


class newsItem(object):
    Id = 0
    header = ''
    link = ''

    def __init__(self, newsId, header, link):
        self.Id = newsId
        self.header = header
        self.link = link


fijivillage = req.get("https://fijivillage.com")
isAvailable = fijivillage.status_code
html = fijivillage.text
newsList = []

if isAvailable == 200:
    parsed_html = bs(html, "html.parser")
    alldiv = parsed_html.find_all('div')

    for div in alldiv:
        isFound = False
        if div.h6:
            story = newsItem(id(div.h6.string), div.h6.string, div.a['href'])
            newsList.append(story)
        elif div.h3:
            story = newsItem(id(div.h3.string), div.h3.string, div.a['href'])
            newsList.append(story)

conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS NEWS
         (ID INT PRIMARY KEY     NOT NULL,
         HEADER           TEXT     NULL,
         LINK            BLOB      NULL);''')
print("Table created successfully")

for item in newsList:
    query = f'INSERT OR IGNORE INTO NEWS (ID,HEADER,LINK) \
          VALUES \
        ({item.Id}, "{item.header}", "{item.link}");'
    conn.execute(query)

conn.commit()
print("Records created successfully")
conn.close()
