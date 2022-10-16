import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil


class ScrapBook:
    def __init__(self):
        """
        Extraction des données sur l'url des ouvrages et repertorie ces données dans des listes.
        """
        self.upc_list = []
        self.price_excl_list = []
        self.price_incl_list = []
        self.available_list = []
        self.describe_list = []
        self.rating_list = []
        self.img_url_list = []

    def extract_all(self, url):
        """
        Actualise la page consultée par beautifullsoup et l'url qui est consulté.
        Méthode permettant en une méthode d'appeler plusieurs autres méthodes, ici :
        self.extract_upc(soup)
        self.extract_price_excl(soup)
        self.extract_price_incl(soup)
        self.extract_available(soup)
        self.extract_rating(soup)
        self.extract_describe(soup)
        self.extract_img_url(soup)
        :param url: str
        """
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        self.extract_upc(soup)
        self.extract_price_excl(soup)
        self.extract_price_incl(soup)
        self.extract_available(soup)
        self.extract_rating(soup)
        self.extract_describe(soup)
        self.extract_img_url(soup)

    def extract_upc(self, soup):
        """
        Extraction de l'upc de l'ouvrage et repertorie cette donnée dans la liste correspondante.
        :param soup: str
        """
        self.upc_list.append(soup.find("table", class_="table table-striped").find("th", text="UPC").findNext("td").text)

    def extract_price_excl(self, soup):
        """
        Extraction de du prix hors taxe de l'ouvrage et repertorie cette donnée dans la liste correspondante.
        :param soup: str
        """
        self.price_excl_list.append(soup.find("table", class_="table table-striped").find("th", text="Price (excl. tax)").findNext("td").text)

    def extract_price_incl(self, soup):
        """
        Extraction du prix taxe comprise de l'ouvrage et repertorie cette donnée dans la liste correspondante.
        :param soup: str
        """
        self.price_incl_list.append(soup.find("table", class_="table table-striped").find("th", text="Price (incl. tax)").findNext("td").text)

    def extract_available(self, soup):
        """
        Extraction de la disponibilité de l'ouvrage et repertorie cette donnée dans la liste correspondante.
        :param soup: str
        """
        self.available_list.append(soup.find("table", class_="table table-striped").find("th", text="Availability").findNext("td").text)

    def extract_rating(self, soup):
        """
        Extraction de la notation des consommateurs de l'ouvrage et repertorie cette donnée
        dans la liste correspondante.
        :param soup: str
        """
        self.rating_list.append(soup.find("p", class_="star-rating")["class"][1])

    def extract_describe(self, soup):
        """
        Extraction de la description de l'ouvrage et repertorie cette donnée dans la liste correspondante.
        :param soup: str
        """
        self.describe_list.append(soup.find("meta", attrs={"name": "description"})["content"].strip())

    def extract_img_url(self, soup):
        """
        Extraction de l'url de l'image correspondant à l'ouvrage et repertorie cette donnée
        dans la liste correspondante.
        :param soup: str
        """
        self.img_url_list.append(soup.find("img")["src"].replace("../../", "http://books.toscrape.com/"))
