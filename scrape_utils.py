import requests
from newspaper import Article, Config, Source
from waybackpy import Url
from time import sleep
from random import randint


def get_article(url):
    article=Article(url)
    article.download()
    article.parse()
    return article.text

class wayback_scraper:
    def __init__(self, url, agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'):
        self.agent=agent
        self.wayback_obj = Url(url, agent)
        self.wayback_url = None
    
    def set_date(self, y, m, d):
        self.wayback_url = str(self.wayback_obj.near(year=y, month=m, day=d))
        
    def get_articles(self, timeout=None):
        #Returns a list of newspaper articles
        
        if self.wayback_url == None:
            raise ValueError("Must set date with set_date function")
        
        config = Config()
        config.browser_user_agent = self.agent
        config.request_timeout = timeout
        
        wayback = Source(url=self.wayback_url, config=config,
                  memoize_articles=False, language='en', number_threads=20, thread_timeout_seconds=2)

        wayback.build()
        
        return wayback.articles
    
    def search(self, keyword):
        
        articles=self.get_articles()
        ret_articles = []
        
        for article in articles:
            if type(article.title) == str:
                if keyword in article.title:
                    ret_articles.append(article)
        
        return ret_articles
            
        
        
        


