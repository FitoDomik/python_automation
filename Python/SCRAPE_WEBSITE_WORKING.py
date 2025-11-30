import urllib.request
from bs4 import BeautifulSoup
import requests
class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        print(sp)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)
news = "https://news.google.com/"
Scraper(news).scrape()
class cloud:
    def __init__(self, value):
        self.value = value
    def hello(self):
        print(self.value)
test="DevOps a gaya"
cloud(test).hello()