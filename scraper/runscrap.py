import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil

class RunScrap:
    def __init__(self):

    def check_repertory(self):
        if not os.path.exists("doc_img"):
            os.mkdir("doc_img")

    def running(self):
        self.generate_nav()
        for url_nav in self.urls_nav:
            self.running_url()
            self.check_repertory()
            self.running_scrap_csv()
            self.load_data_csv()
            self.running_scrap_load_img()