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

Un dossier nommé scrap_doc sera créé dans le repository principal.
Ce dossier sera composé de sous_dossié portant le nom des différentes catégories de livres.
Chacun de ces sous dossier contiendra un fichier csv avec tous les livres relatifs à cette catégorie et les données relatives à ces livres (voir 1/)
Chacun de ces sous dossier contiendra aussi les images relatives aux livres repertoriés dans le fichier csv (voir 2/)


Si vous désirez d'avantage d'informations sur les composantes des classes et modules utilisés dans le script de la pipeline ETL,
merci de consulter la documentation (docs/_build/html/index.html) proposée dans le repository principal

UTILISATION:
Voici les étapes à réaliser pour utiliser la pipeline ETL :

- Dans votre terminal, accédez au dossier projet_2_OC :
    Saisissez dans votre terminal : `cd nom_du_chemin_d_acces` 
    Si vous recherchez le path de ce chemin, allez dans le dossier projet_2_OC, et dans la barre de recherche du dossier,
        situé en haut du dossier, faites un clic gauche pour sélectionner le chemin, puis un clic droit pour copier coller ce chemin
- Dans votre terminal, créez un environnement virtuel pour Python, par convention nous appelerons cet environnement : env
    * Sous Microsoft Windows : `python -m venv env`
    * Sous Linux et Mac : `python3 -m venv env`
- Connectez vous à cet environnement virtuel :
    * Sur un terminal Windows powershell : `env/Scripts/Activate.ps1`
    * Sur un terminal Windows invite de commande : `env/Scripts/activate.bat`
    * Sur un terminal Linux ou Mac : `source env/bin/activate`
- Vérifiez que vous êtes bien connecté à votre environnement virtuel, au début de la ligne du terminal doit apparaître : (env)
    Si vous désirez vous déconnecter de votre environnement virtuel, saisissez la commande : `deactivate`
- Installez dans votre environnement virtuel les modules attendus pour le bon fonctionnement du script de la pipeline ETL :
    Une fois connecté à votre environnement virtuel saisissez dans votre terminal la commande : `pip install -r requirements.txt`
- Vous pouvez maintenant lancer le processus d'extraction des données en saisissant dans votre terminal :
    * Sur Microsoft Windows : `python main.py`
    * Sur Linux ou Mac : `python3 main.py`

Pour toute problématique de lancement lié à l'installation de Python ou des Path liés à Microsoft, Mac ou Linux,
Merci de vous référez directement au site officiel de Python : https://www.python.org/downloads/

LICENSE:
Application open source

REQUIREMENTS:
Python 3.X, modules (merci de consulter le fichier: requirements.txt)

```Python
print("hello")
# commentaire
```