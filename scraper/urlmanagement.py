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

    def generate_urls_nav(self):
        for i in self.soup.find("div", class_="side_categories").find_all("a"):
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
