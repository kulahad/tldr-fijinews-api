from abc import ABC,abstractmethod
import requests
from bs4 import BeautifulSoup
from summarize import summarizetext
from models import News



class extractor(ABC):
    def __init__(self):
        self.url = ""

    @abstractmethod
    def htmlparser(self):
        pass

    def savetodb(self, data):
        # save all data to db
        print("Sending data to DB")

    def extracthtml(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, "html.parser")
    
    def run(self):
        data = self.htmlparser()
        self.savetodb(data=data)




class fijivillage(extractor):
    def __init__(self):
        self.url = "https://fijivillage.com/news"
        self.source = "Fijivillage"

    def htmlparser(self):
        content = self.extracthtml()
        # only process 10 articles
        newsdivs = content.find_all("div", class_="col-md-4 pt-2")[:10]
        news = []

        for div in newsdivs:
            news.append(self.extractinfo(divdata=div))
        
        return news

    def extractinfo(self,divdata):
        try:
            soup = BeautifulSoup(str(divdata), "html.parser")
            
            # Extract the article URL and title
            article_link = soup.find('a', href=True)
            article_url = article_link['href'] if article_link else None
            title_tag = soup.find('h6')
            article_title = title_tag.text.strip() if title_tag else None
            
            # Extract the image URL
            img_tag = soup.find('img')
            image_url = img_tag.get('src') if img_tag else None

            # get article from url
            page = BeautifulSoup(requests.get(article_url).content, "html.parser")
            article = page.find("div", class_="news_reader")

            time_span = page.find('span', class_="greytime2")
            time = time_span.get_text()

            summary = summarizetext(article.text)
            
            return {
                'id':article_url,
                'title': article_title,
                'summary': summary,
                'article_url': article_url,
                'publish_time': time,
                'image_url': image_url,
                'source': self.source
            }
        except Exception as e:
            print(f"Error parsing HTML snippet: {e}")
            return None
    

if __name__ == "__main__":
    test = fijivillage()
    test.run()