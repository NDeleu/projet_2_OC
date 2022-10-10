import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import os
import shutil

class UrlManagement:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.urls_nav = []
        self.titles_nav = []
        self.last_url = "index.html"
        self.id_titles = 0
        self.titles_nav_pages = []
        self.titles_books = []
        self.urls_books = []

    def generate_urls_nav(self):
        check_etape_zero = 0
        for i in self.soup.find("div", class_="side_categories").find_all("a"):
            print(str(check_etape_zero), " /51, etape 0/4")
            check_etape_zero += 1
            self.urls_nav.append(i["href"])
        for i in range(len(self.urls_nav)):
            self.urls_nav[0+i] = self.url + self.urls_nav[0+i]
        del self.urls_nav[0]

    def generate_titles_nav(self):
        for i in self.soup.find("div", class_="side_categories").find_all("a"):
            self.titles_nav.append(i.text)
        for i in range(len(self.titles_nav)):
            self.titles_nav[0 + i] = self.titles_nav[0 + i].strip()
        del self.titles_nav[0]

    def generate_nav(self):
        self.generate_urls_nav()
        self.generate_titles_nav()

    def update_soup(self):
        check_etape_un = 0
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        for i in self.soup.find_all("h3"):
            print(str(check_etape_un), " /1000, etape 1/4")
            check_etape_un += 1
            self.titles_books.append(i.a["title"])
            self.urls_books.append(i.a["href"].replace("../../../", "http://books.toscrape.com/catalogue/"))
            self.generate_titles_nav_pages()

    def generate_titles_nav_pages(self):
        self.titles_nav_pages.append(self.titles_nav[self.id_titles])

    def test_next(self):
        if self.soup.find(class_="next"):
            self.next_page()
        else:
            pass

    def running_url(self):
        self.generate_nav()
        for url_nav in self.urls_nav:
            self.url = url_nav
            self.last_url = "index.html"
            self.url = self.url.replace("index.html", self.last_url)
            self.update_soup()
            self.test_next()
            self.id_titles += 1

    def next_page(self):
        add_url = self.soup.find(class_="next").a["href"]
        self.url = self.url.replace(self.last_url, add_url)
        self.update_soup()
        self.last_url = add_url
        self.test_next()

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

            check_etape_trois = 0

            for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, \
                number_available, product_description, category, review_rating, image_url \
                in zip(self.scrap_url.urls_books, self.scrap_book.upc_list, self.scrap_url.titles_books, self.scrap_book.price_incl_list,
                       self.scrap_book.price_excl_list, self.scrap_book.available_list, self.scrap_book.describe_list,
                       self.scrap_url.titles_nav_pages, self.scrap_book.rating_list, self.scrap_book.img_url_list):

                print(str(check_etape_trois), " /1000, etape 3/4")
                check_etape_trois += 1

                ligne = [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                         number_available, product_description, category, review_rating, image_url]
                writer.writerow(ligne)

    def running_scrap_csv(self):
        check_etape_deux = 0
        self.scrap_url.running_url()
        for url_book in self.scrap_url.urls_books:
            print(str(check_etape_deux), " /1000, etape 2/4")
            check_etape_deux += 1
            self.scrap_book.extract_all(url_book)

    def running_scrap_load_img(self):
        if not os.path.exists("doc_img"):
            os.mkdir("doc_img")

        check_etape_quatre = 0

        for url in self.scrap_book.img_url_list:
            print(str(check_etape_quatre), " /1000, etape 4/4")
            check_etape_quatre += 1
            with Image.open(requests.get(url, stream=True).raw) as img:
                img.save(self.scrap_book.upc_list[self.id_upc]+".jpg")
                shutil.copy(self.scrap_book.upc_list[self.id_upc]+".jpg", "doc_img/"+self.scrap_book.upc_list[self.id_upc]+".jpg")
                os.remove(self.scrap_book.upc_list[self.id_upc]+".jpg")
            self.id_upc += 1

    def running(self):
        self.running_scrap_csv()
        self.load_data_csv()
        self.running_scrap_load_img()


scrap = LoadScrap("http://books.toscrape.com/")
scrap.running()
print("Scrape completed")