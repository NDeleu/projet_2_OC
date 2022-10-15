import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil


class LoadImage:
    def __init__(self):


    def running_scrap_load_img(self):
        id_upc = 0
        for url in self.scrap_book.img_url_list:
            with Image.open(requests.get(url, stream=True).raw) as img:
                img.save(self.scrap_book.upc_list[self.id_upc] + ".jpg")
                shutil.copy(self.scrap_book.upc_list[self.id_upc] + ".jpg",
                            "doc_img/" + self.scrap_book.upc_list[self.id_upc] + ".jpg")
                os.remove(self.scrap_book.upc_list[self.id_upc] + ".jpg")
            id_upc += 1