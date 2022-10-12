import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil

class ScrapBook:
    """
    Extracts elements from the page
    """
    def __init__(self):
        self.upc_list = []
        self.price_excl_list = []
        self.price_incl_list = []
        self.available_list = []
        self.describe_list = []
        self.rating_list = []
        self.img_url_list = []

    def extract_all(self, url):
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
        self.upc_list.append(soup.find("table", class_="table table-striped").find("th", text="UPC").findNext("td").text)

    def extract_price_excl(self, soup):
        self.price_excl_list.append(soup.find("table", class_="table table-striped").find("th", text="Price (excl. tax)").findNext("td").text)

    def extract_price_incl(self, soup):
        self.price_incl_list.append(soup.find("table", class_="table table-striped").find("th", text="Price (incl. tax)").findNext("td").text)

    def extract_available(self, soup):
        self.available_list.append(soup.find("table", class_="table table-striped").find("th", text="Availability").findNext("td").text)

    def extract_rating(self, soup):
        self.rating_list.append(soup.find("p", class_="star-rating")["class"][1])

    def extract_describe(self, soup):
        self.describe_list.append(soup.find("meta", attrs={"name": "description"})["content"].strip())

    def extract_img_url(self, soup):
        self.img_url_list.append(soup.find("img")["src"].replace("../../", "http://books.toscrape.com/"))
