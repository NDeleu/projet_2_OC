from scraper import LoadScrap

scrap = LoadScrap("http://books.toscrape.com/")
scrap.running()
print("Scrape completed")