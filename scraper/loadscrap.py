import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil
from .scrapbook import ScrapBook
from .urlmanagement import UrlManagement

class LoadScrap:
    def __init__(self, url):
        self.url = url
        self.en_tete_csv = ["product_page_url", "universal_product_code", "title", "price_including_tax",
                            "price_excluding_tax", "number_available", "product_description", "category",
                            "review_rating", "image_url"]
        self.id_upc = 0
        self.scrap_url = UrlManagement(self.url)
        self.scrap_book = ScrapBook()

    def load_data_csv(self):
        with open("data.csv", "w+", newline='', encoding="utf-8") as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=',')
            writer.writerow(self.en_tete_csv)

            for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, \
                number_available, product_description, category, review_rating, image_url \
                in zip(self.scrap_url.urls_books, self.scrap_book.upc_list, self.scrap_url.titles_books, self.scrap_book.price_incl_list,
                       self.scrap_book.price_excl_list, self.scrap_book.available_list, self.scrap_book.describe_list,
                       self.scrap_url.titles_nav_pages, self.scrap_book.rating_list, self.scrap_book.img_url_list):

                ligne = [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                         number_available, product_description, category, review_rating, image_url]
                writer.writerow(ligne)

    def running_scrap_csv(self):
        self.scrap_url.running_url()
        for url_book in self.scrap_url.urls_books:
            self.scrap_book.extract_all(url_book)
