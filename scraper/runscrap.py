import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil

from .urlmanagement import UrlManagement
from .scrapbook import ScrapBook

class RunScrap:
    def __init__(self, url):
        self.url = url
        self.scrap_url = UrlManagement(self.url)
        self.scrap_book = ScrapBook()

    def check_repertory(self, category):
        if not os.path.exists(category,"_doc"):
            os.mkdir(category,"_doc")

    def running_scrap_csv(self):
        self.scrap_url.running_url()
        for url_book in self.scrap_url.urls_books:
            self.scrap_book.extract_all(url_book)

    def running(self):
        self.scrap_url.generate_nav()
        for url_nav in self.urls_nav:
            self.check_repertory(self.titles_nav[self.id_titles])
            self.running_url()

            self.running_scrap_csv()
            self.load_data_csv()
            self.running_scrap_load_img()