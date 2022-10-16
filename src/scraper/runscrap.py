import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil

from .urlmanagement import UrlManagement
from .scrapbook import ScrapBook
from .checknextpage import CheckNext
from .loadscrap import LoadScrap
from .loadimage import LoadImage


class RunScrap:
    def __init__(self, url):
        """
        Centralise les classes et les méthodes de l'application de la pipeline ETL.
        Permet d'executer l'ensemble des méthodes de l'application à partir de cette classe.
        Création des dossiers répertoriant les données et images extraits.
        Récupère l'url correspondant au site Book to Scrape
        :param url: str
        """
        self.url = url
        self.urls_nav_mng = UrlManagement(self.url)
        self.scrap_url = None
        self.scrap_book = None
        self.load_scrap = LoadScrap()
        self.load_image = LoadImage()
        self.id_titles = 0

    def check_main_repertory(self):
        """
        Vérification de l'existance d'un dossier repertoriant l'ensemble des données et images extrait, et création
        de ce dossier si inexistant a priori
        """
        if not os.path.exists("scrap_doc"):
            os.mkdir("scrap_doc")

    def check_repertory(self, title_nav):
        """
        Vérification de l'existance d'un dossier repertoriant les données et images relatives à la catégorie
        renseignée par title_nav, et création de ce dossier si inexistant a priori
        :param title_nav: str
        """
        if not os.path.exists("scrap_doc/" + title_nav + "_doc"):
            os.mkdir("scrap_doc/" + title_nav + "_doc")

    def running_scrap_csv(self, url_nav, title_nav):
        """
        Méthode créant les instances de ScrapBook et de CheckNext pour les réactualiser à chaque catégories
        renseignées par l'instance d'UrlManagement et qui seront utilisés dans la méthode running().
        Cette méthode appelera la méthode running_url() de l'instance de la classe CheckNext pour renseigner
        l'url de la méthode extract_all de l'instance de la classe ScrapBook afin d'extraire les données désirées
        sur chaque url correspondant aux ouvrages.
        :param url_nav: str
        :param title_nav: str
        """
        self.scrap_url = CheckNext(url_nav, title_nav)
        self.scrap_url.running_url()
        self.scrap_book = ScrapBook()
        for url_book in self.scrap_url.urls_books:
            self.scrap_book.extract_all(url_book)

    def running(self):
        """
        Méthode principale de l'application faisant appelle aux autres méthodes.
        Dans l'ordre la méthode appelera :
        - la vérification et, sous condition, la création du dossier repertoriant l'ensemble des données extraites,
        - génèrera les listes des url et titres des catégories,
        - pour chaque catégorie, la méthode pour vérifier et, sous condition créer le sous dossier de la catégorie,
        - l'extraction des données pour chaque catégorie
        - l'écriture de ces données dans un fichier csv repertorié dans le sous dossier de la catégorie relative
        - l'extraction et l'enregistrement des images correspondantes aux ouvrages dans le sous dossier de la
        catégorie relative.
        Enfin la méthode fait appel à une accrémentation d'un id : self.id_titles pour itérer l'indice des listes
        dans l'ordre.
        """
        self.check_main_repertory()
        self.urls_nav_mng.generate_nav()
        for url_nav in self.urls_nav_mng.urls_nav:
            self.check_repertory(self.urls_nav_mng.titles_nav[self.id_titles])
            self.running_scrap_csv(url_nav, self.urls_nav_mng.titles_nav[self.id_titles])

            self.load_scrap.load_data_csv(self.scrap_url, self.scrap_book, self.urls_nav_mng.titles_nav[self.id_titles])
            self.load_image.running_scrap_load_img(self.scrap_book, self.urls_nav_mng.titles_nav[self.id_titles])

            self.id_titles += 1