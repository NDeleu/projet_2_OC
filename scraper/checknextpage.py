import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil


class CheckNext:
    def __init__(self, url_nav, title_nav):
        self.url = url_nav
        self.title_nav = title_nav
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.last_url = "index.html"
        self.titles_nav_pages = []
        self.titles_books = []
        self.urls_books = []

    def update_soup(self):
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        for i in self.soup.find_all("h3"):
            self.titles_books.append(i.a["title"])
            self.urls_books.append(i.a["href"].replace("../../../", "http://books.toscrape.com/catalogue/"))
            self.generate_titles_nav_pages()

    def generate_titles_nav_pages(self):
        self.titles_nav_pages.append(self.title_nav)

    def test_next(self):
        if self.soup.find(class_="next"):
            self.next_page()
        else:
            pass

    def running_url(self):
        self.last_url = "index.html"
        self.url = self.url.replace("index.html", self.last_url)
        self.update_soup()
        self.test_next()

    def next_page(self):
        add_url = self.soup.find(class_="next").a["href"]
        self.url = self.url.replace(self.last_url, add_url)
        self.update_soup()
        self.last_url = add_url
        self.test_next()

