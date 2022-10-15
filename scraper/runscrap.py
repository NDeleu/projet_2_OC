import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil

from .urlmanagement import UrlManagement
from .scrapbook import ScrapBook
from .checknextpage import CheckNext


class RunScrap:
    def __init__(self, url):
        self.url = url
        self.urls_nav_mng = UrlManagement(self.url)
        self.scrap_url = None
        self.scrap_book = None
        self.id_titles = 0

    def check_repertory(self, title_nav):
        if not os.path.exists(title_nav + "_doc"):
            os.mkdir(title_nav + "_doc")

    def running_scrap_csv(self, url_nav, title_nav):
        self.scrap_url = CheckNext(url_nav, title_nav)
        self.scrap_url.running_url()
        self.scrap_book = ScrapBook()
        for url_book in self.scrap_url.urls_books:
            self.scrap_book.extract_all(url_book)

    def running(self):
        self.urls_nav_mng.generate_nav()
        for url_nav in self.urls_nav_mng.urls_nav:
            self.check_repertory(self.urls_nav_mng.titles_nav[self.id_titles])
            self.running_scrap_csv(url_nav, self.urls_nav_mng.titles_nav[self.id_titles])

            self.load_data_csv(self.urls_nav_mng, self.scrap_book)
            self.running_scrap_load_img()

            self.id_titles += 1