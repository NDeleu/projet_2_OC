DESCRIPTION:
Pipeline ETL du site Books to Scrape : http://books.toscrape.com/

composante des éléments extraits :

1/
	- product_page_url		Lien URL de la page de l'ouvrage
	- universal_product_code	Code UPC de l'ouvrage
	- title				Titre de l'ouvrage
	- price_including_tax		Prix TTC
	- price_excluding_tax		Prix HT
	- number_available		Nombre ddisponible de l'ouvrage
	- product_description		Description de l'ouvrage
	- category			Catégorie de l'ouvrage selon le site Books to Scrape
	- review_rating			Notation de l'ouvrage selon les lecteurs
	- image_url			Lien URL de l'image correspondant à l'ouvrage

2/
	- image				image format jpg correspondante à l'ouvrage

1/ Toutes les données de cette partie seront enregistrés dans un fichier csv nommé data.csv
2/ Un dossier nommé doc_img sera créé lors du processus de l'extraction des données pour enregistrer les images

Le processus d'extraction peut être suivit en temps réel directement sur la console/terminal d'éxecution.
Ce processus est défini en 5 points :
	- extraction de l'URL des différentes catégories
	- extraction de l'URL des différents ouvrages
	- extraction des données des ouvrages
	- enregistrement de toutes les données (1/) dans le fichier data.csv
	- enregistrement de toutes les images (2/)  dans le document doc_img

Si vous désirez d'avantage d'informations sur les composantes des classes et modules, merci de consulter la documentation (doc) 

LICENSE:
Application open source

REQUIREMENTS:
Python 3.X, modules (merci de consulter le fichier: requirements.txt)