import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil


class CheckNext:
    def __init__(self, url_nav, title_nav):
        """
        Extraction des Titres des ouvrages et des urls de ces ouvrages qui sont ensuite enregistrés dans des listes.
        Création d'une liste reprenant les titres des catégories pour
        les itérer en autant d'exemplaires que d'ouvrages correspondants.
        Remonte toutes les pages d'une catégories en vérifiant si l'attribut next existe sur la page html consultée
        :param url_nav: str
        :param title_nav: str
        """
        self.url = url_nav
        self.title_nav = title_nav
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.last_url = "index.html"
        self.titles_nav_pages = []
        self.titles_books = []
        self.urls_books = []

    def update_soup(self):
        """
        Actualise la page consultée par beautifullsoup en actualisant l'url consulté.
        Ajoutes aux listes de la classe : le titre (nom) des ouvrage, l'url de leur page et le titre (nom)
        des catégories de livre par itération.
        """
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        for i in self.soup.find_all("h3"):
            self.titles_books.append(i.a["title"])
            self.urls_books.append(i.a["href"].replace("../../../", "http://books.toscrape.com/catalogue/"))
            self.titles_nav_pages.append(self.title_nav)

    def test_next(self):
        """
        Méthode vérifiant si l'attribut next existe sur la page html consulté, si ce n'est pas le cas cela permet
        de mettre fin à la boucle de la catégorie consulté, alors que si c'est le cas la boucle de cette catégorie
        continuera avec la page suivante appartenant à la même catégorie de livres appelant la méthode next_page()
        """
        if self.soup.find(class_="next"):
            self.next_page()
        else:
            pass

    def running_url(self):
        """
        Méthode préparant les compléments d'adresses url pour la méthode next-page() et
        permettant aussi en une méthode d'appeler plusieurs autres méthodes, ici :
        self.update_soup()
        self.test_next()
        """
        self.last_url = "index.html"
        self.url = self.url.replace("index.html", self.last_url)
        self.update_soup()
        self.test_next()

    def next_page(self):
        """
        Appelée par la méthode test_next() si l'attribut next, de la page html consultée, existe,
        cette méthode permet de modifier le complément de l'url pour appeler la page suivante de la même catégorie
        """
        add_url = self.soup.find(class_="next").a["href"]
        self.url = self.url.replace(self.last_url, add_url)
        self.update_soup()
        self.last_url = add_url
        self.test_next()

