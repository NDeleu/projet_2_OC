import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil


class LoadImage:
    def __init__(self):
        pass

    def running_scrap_load_img(self, scrap_book, category_title):
        id_upc = 0
        for url in scrap_book.img_url_list:
            with Image.open(requests.get(url, stream=True).raw) as img:
                img.save(scrap_book.upc_list[id_upc] + ".jpg")
                shutil.copy(scrap_book.upc_list[id_upc] + ".jpg",
                            category_title + "_doc/" + scrap_book.upc_list[id_upc] + ".jpg")
                os.remove(scrap_book.upc_list[id_upc] + ".jpg")
            id_upc += 1