import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil


class LoadImage:
    def __init__(self):
        """
        Recherche les images à partir de la liste des url d'image proposée par ScrapBook et extrait ces images
        en les nommant par l'upc de l'ouvrage correspondant
        """
        pass

    def running_scrap_load_img(self, scrap_book, category_title):
        """
        A partir de l'instance de ScrapBook pour accéder à la liste des url des images
        et à la liste des upc correspondant, ainsi qu'à partir de l'instance de CheckNext
        pour extraire le titre des catégories, les images relatives aux ouvrages seront extraites et enregistrées
        en format jpg avec le nom de l'upc de l'ouvrage relatif dans le dossier au nom de catégorie correspodant.
        :param scrap_book: str
        :param category_title: str
        """
        id_upc = 0
        for url in scrap_book.img_url_list:
            with Image.open(requests.get(url, stream=True).raw) as img:
                img.save(scrap_book.upc_list[id_upc] + ".jpg")
                shutil.copy(scrap_book.upc_list[id_upc] + ".jpg",
                            "scrap_doc/" + category_title + "_doc/" + scrap_book.upc_list[id_upc] + ".jpg")
                os.remove(scrap_book.upc_list[id_upc] + ".jpg")
            id_upc += 1