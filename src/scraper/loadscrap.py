import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil


class LoadScrap:
    def __init__(self):
        """
        Ecrit les données extraites dans un fichier csv relatif à la catégorie des ouvrages et distribué en
        fonction des éléments repertoriés dans la liste self.en_tete_csv
        """
        self.en_tete_csv = ["product_page_url", "universal_product_code", "title", "price_including_tax",
                            "price_excluding_tax", "number_available", "product_description", "category",
                            "review_rating", "image_url"]

    def load_data_csv(self, scrap_url, scrap_book, category_title):
        """
        Récupère les données extraites et repertoriées dans les listes des classes CheckNext et ScrapBook et écrit
        ces données dans un fichier csv qui prendra le nom de la catégorie des ouvrages correspondante
        :param scrap_url: str
        :param scrap_book: str
        :param category_title: str
        """
        with open("scrap_doc/" + category_title + "_doc/" + category_title + ".csv",
                  "w+", newline='', encoding="utf-8") as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=',')
            writer.writerow(self.en_tete_csv)

            for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, \
                number_available, product_description, category, review_rating, image_url \
                in zip(scrap_url.urls_books, scrap_book.upc_list, scrap_url.titles_books, scrap_book.price_incl_list,
                       scrap_book.price_excl_list, scrap_book.available_list, scrap_book.describe_list,
                       scrap_url.titles_nav_pages, scrap_book.rating_list, scrap_book.img_url_list):

                ligne = [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                         number_available, product_description, category, review_rating, image_url]
                writer.writerow(ligne)


