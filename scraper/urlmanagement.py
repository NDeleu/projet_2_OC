import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil

class UrlManagement:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.urls_nav = []
        self.titles_nav = []
        self.last_url = "index.html"
        self.id_titles = 0
        self.titles_nav_pages = []
        self.titles_books = []
        self.urls_books = []

    def generate_urls_nav(self):
        check_etape_un = 0
        for i in self.soup.find("div", class_="side_categories").find_all("a"):
            print(str(check_etape_un), " /50, etape 1/5")
            check_etape_un += 1
            self.urls_nav.append(i["href"])
        for i in range(len(self.urls_nav)):
            self.urls_nav[0+i] = self.url + self.urls_nav[0+i]
        del self.urls_nav[0]

    def generate_titles_nav(self):
        for i in self.soup.find("div", class_="side_categories").find_all("a"):
            self.titles_nav.append(i.text)
        for i in range(len(self.titles_nav)):
            self.titles_nav[0 + i] = self.titles_nav[0 + i].strip()
        del self.titles_nav[0]

    def generate_nav(self):
        self.generate_urls_nav()
        self.generate_titles_nav()

    def update_soup(self):
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        for i in self.soup.find_all("h3"):
            self.titles_books.append(i.a["title"])
            self.urls_books.append(i.a["href"].replace("../../../", "http://books.toscrape.com/catalogue/"))
            self.generate_titles_nav_pages()

    def generate_titles_nav_pages(self):
        self.titles_nav_pages.append(self.titles_nav[self.id_titles])

    def test_next(self):
        if self.soup.find(class_="next"):
            self.next_page()
        else:
            pass

    def running_url(self):
        check_etape_deux = 0
        self.generate_nav()
        for url_nav in self.urls_nav:
            print(str(check_etape_deux), " /1000, etape 2/5")
            check_etape_deux += 1
            self.url = url_nav
            self.last_url = "index.html"
            self.url = self.url.replace("index.html", self.last_url)
            self.update_soup()
            self.test_next()
            self.id_titles += 1

    def next_page(self):
        add_url = self.soup.find(class_="next").a["href"]
        self.url = self.url.replace(self.last_url, add_url)
        self.update_soup()
        self.last_url = add_url
        self.test_next()